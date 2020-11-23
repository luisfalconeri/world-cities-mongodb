from app_src import mongo_geo_db as mongo
from app_src.utils.world_cities_mongodb.helpers.parser import cities, countries, cities_dict, countries_dict
import urllib3
from urllib.parse import quote_plus
from app_src.utils.world_cities_mongodb import settings

CITY_COLLECTION = mongo["letter-app"].cities
COUNTRY_COLLECTION = mongo["letter-app"].countries

def init():
    CITY_COLLECTION.drop()
    COUNTRY_COLLECTION.drop()

#################
#  Save cities  #
#################

def add_extra_country_fields():
    if not settings.ADD_COUNTRY_TO_CITY:
        return

    for city in cities:
        according_country = countries_dict[city['country_code']]
        attrs_to_add = {
            'country_id': according_country.country_id
        }
        for attr in settings.COUNTRY_FIELDS_TO_ADD:
            attrs_to_add[attr] = getattr(according_country, attr)

        city['country'] = attrs_to_add

def save_cities():
    add_extra_country_fields()
    save_to_db(CITY_COLLECTION, cities)

def add_extra_cities_fields():
    if not settings.ADD_CITY_TO_COUNTRY:
        return
    
    for country in countries:
        if country['iso'] in cities_dict:
            country['cities'] = cities_dict[country['iso']]

####################
#  Save countries  #
####################

def save_countries():
    add_extra_cities_fields()
    save_to_db(COUNTRY_COLLECTION, countries)

def save_to_db(mongo_collection, data):
    if not isinstance(data, list):
        raise ValueError('Except data to be a list')

    if not isinstance(data[0], dict):
        raise ValueError('Except item of data to be a dict')

    mongo_collection.insert_many(data)
