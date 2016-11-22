
import json
import httplib

class RestResponse:
    __entity = {}

    def __init__(self, data={}, status = httplib.OK, messages=None, success = True):
        '''
        
        :param data: Response data of Rest call.
        :param status: Response status of Rest call , default is 1 means success.
        :param messages: Response message of Rest call , default is None.
        '''
        self.__entity['data'] = data
        self.__entity['status'] = status
        self.__entity['messages'] = messages
        self.__entity['success'] = success
        
    def to_json(self):
        '''
        :return json-encoded.
        '''
        return json.dumps(self.__entity)
    
    
def singleton(class_):
    '''
    
    :param class_:class .
    :return singleton instance of class .
    '''
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


    