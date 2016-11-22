from config import db ,STORES
from validator import Store
from grampower.db_manager import AbstractBaseService
import httplib
from grampower.utils import RestResponse, singleton
import os
import urllib
from PIL import Image
from resizeimage import resizeimage
from bson.objectid import ObjectId
import logging

@singleton
class StoreService(AbstractBaseService):
    
    # @Override
    def db(self):
        return db[STORES]
    
    def register(self,store):
        
        if self.db().find_one({Store.LICENCE_NO:store[Store.LICENCE_NO]}) is None:
            store =  self.save(store) 
            
            store[Store.COVER_IMAGE] = self._download_images_locally(store[Store.COVER_IMAGE],  store[Store.ID], cover_image =True)
            images = []
            for image in store[Store.THUMBNAILS]:
                images.append( self._download_images_locally(image, store[Store.ID]))
            store[Store.THUMBNAILS] = images
            store[Store.ID]=ObjectId(store[Store.ID])
            updated_store =  self.save(store) 
            updated_store[Store.ID] = str(store[Store.ID])
            
            return RestResponse(store).to_json()
        else:
            return RestResponse(messages ="store already exist." ,status = httplib.CONFLICT, data = None, success = False).to_json()
        
    
    def find_store_by_id(self,store_id):
        
        store = self.find_one(store_id)
        if store is not None:
            store[Store.ID] = str(store[Store.ID])
            return RestResponse(store).to_json()
        else:
            return RestResponse(messages ="store not found", status = httplib.NOT_FOUND, data = None, success = False).to_json()
        
        
    def find_stores_pagination(self,page):
        
        store_list = []
        stores = self.find_all(page)
        for store in stores:
            store[Store.ID] = str(store[Store.ID])
            store_list.append(store)
        return store_list    


    def _download_images_locally(self, url, store_id, cover_image = False):
    
        cwd = os.getcwd()
        if not os.path.exists('grampower/static/img'):
            os.makedirs('grampower/static/img')
            
        if not os.path.exists('grampower/static/thumbnail'):
            os.makedirs('grampower/static/thumbnail')
        
        if cover_image:
            filename = str(store_id)+"_coverImage.jpg"
            os.chdir('grampower/static/img')
            urllib.urlretrieve(url, filename)
            os.chdir(cwd)
            return os.path.join(os.path.dirname(__file__), "/static/img/"+filename)
        
        else:
            fcount_list = []    
            for f in os.listdir('grampower/static/img' ):
                if f.endswith(".jpg") and str(store_id)+'_image' in f:
                    fcount_list.append(int(f.split('_')[1].split('.')[0][5:]))
            if len(fcount_list)==0:
                count = 1
            else:
                count = max(fcount_list)+1
            filename = str(store_id)+"_image" + str(count)+ ".jpg"
          
            os.chdir('grampower/static/img')
            urllib.urlretrieve(url, filename)
            
            try:
                fd_img = open(filename, 'r')
                img = Image.open(fd_img)
                img = resizeimage.resize_thumbnail(img, [128, 128])
            
                os.chdir('../thumbnail')
                img.save(filename, img.format)
                img.close()
                fd_img.close()
            except Exception as e:
                logging.error(e)
            
            os.chdir(cwd)
            return os.path.join(os.path.dirname(__file__), "/static/thumbnail/"+filename)
              
    
    
    
    
    