from schema import Schema, And, Use, Optional
import json


class Store:

    ID = '_id'
    NAME = 'name'
    STREET_ADDRESS = 'street_address'
    POSTAL_CODE = 'postal_code'
    CITY = 'city'
    COUNTRY = 'country'
    CONTACT_NUMBER = 'contact_number'
    DESCRIPTION = 'description'
    COVER_IMAGE = 'cover_image'
    LICENCE_NO = 'licence_no'
    PRO_CATEGORIES = 'pro_categories'
    THUMBNAILS = 'thumbnails'
    WORKING_DAYS = 'working_days'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'

    VALIDATOR = Schema(And(Use(json.loads), {
        Optional(ID): object,
        NAME: basestring,
        STREET_ADDRESS: basestring,
        POSTAL_CODE:basestring,
        CITY:basestring,
        COUNTRY:basestring,
        CONTACT_NUMBER:basestring,
        LICENCE_NO:basestring,
        Optional(DESCRIPTION):basestring,
        Optional(COVER_IMAGE):basestring,
        Optional(LATITUDE):basestring,
        Optional(LONGITUDE):basestring,
        Optional(PRO_CATEGORIES):list,
        Optional(THUMBNAILS):list,
        Optional(WORKING_DAYS):list
                                             
    }))
