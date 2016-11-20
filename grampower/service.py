from config import db ,STORES
from validator import Store
from grampower.db_manager import AbstractBaseService
import httplib
from grampower.utils import RestResponse, singleton

@singleton
class StoreService(AbstractBaseService):
    
    # @Override
    def db(self):
        return db[STORES]
    
    def register(self,store):
        if self.db().find_one({Store.LICENCE_NO:store[Store.LICENCE_NO]}) is None:
            store =  self.save(store) 
            store[Store.ID] = str(store[Store.ID])
            return RestResponse(messages ="store inserted successfully" ,status = httplib.OK, data = store, success = True).to_json()
        else:
            return RestResponse(messages ="store already exist." ,status = httplib.CONFLICT, data = None, success = False).to_json()
        
    
    def find_store_by_id(self,store_id):
        
        store = self.find_one(store_id)
        if store is not None:
            store[Store.ID] = str(store[Store.ID])
            return store
        else:
            return RestResponse(messages ="store not found", status = httplib.NOT_FOUND, data = None, success = False).to_json()
        
        
    def find_stores_pagination(self,page):
        
        store_list = []
        stores = self.find_all(page)
        for store in stores:
            store[Store.ID] = str(store[Store.ID])
            store_list.append(store)
        return store_list    
