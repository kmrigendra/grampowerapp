from abc import ABCMeta, abstractmethod
from bson.objectid import ObjectId

from config import PAGE_SIZE


class AbstractBaseService(object):
    '''
    A simple abstract base service for CRUD implementations of entities 
    '''
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def db(self):
        '''
        this method returns the mongo collection for the entity
        for e.g. StoreService will return the 'db.store' as the mongo collection.
        '''
        pass

    def find_one(self, entity_id):
        '''

        Queries the db and returns the entity or returns None if nothing found
        :param entity_id: the id to be queried for.
        :type entity_id: String or objectId
        '''
        return self.db().find_one(self.convert_str_id_to_object_id(entity_id))
    
    def find_all(self, page=0, size=PAGE_SIZE):
        '''
        
        :param page: page number 
        :param size: number of records to be fetched
        :return all the paginated entities
        '''
        return self.db().find(skip=page * size, limit=size)

    def save(self, entity):
        '''
        saves a new entity in the database if _id is not present otherwise replaces an existing entity
        :param entity: the entity to be saved in the database
        :returns the full entity along with the generated id success
        '''
            
        entity_id = self.db().save(entity)
        entity['_id'] = entity_id
        return entity
    
    def remove(self, entity_id):
        '''
        Deletes an entity permanently from the database.
        :param entity_id: id of the entity to be deleted
        :type entity_id: string or ObjectId
        :return A document (dict) describing the effect of the remove or 
                ``None`` if write acknowledgment is disabled.
        '''
        return self.db().remove(self.convert_str_id_to_object_id(entity_id))

    
    def convert_str_id_to_object_id(self, str_id):
        if str_id is not isinstance(str_id, ObjectId):
            return ObjectId(str_id)
        return str_id
    
