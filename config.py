import logging
from pymongo import MongoClient
  
# logger
logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='grampower.log',
            filemode='w')

STORES = 'stores' 
  
mongo_client = MongoClient("mongodb://prakash:Sinha1626@ds157487.mlab.com:57487/heroku_j5ncd6ws")
db = mongo_client.get_default_database()

PAGE_SIZE = 10