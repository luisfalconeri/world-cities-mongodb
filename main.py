from app_src.utils.world_cities_mongodb.helpers.mongodb import init, save_cities, save_countries
from app_src.utils.world_cities_mongodb.helpers.parser import parse_city, parse_country, remove_non_match_language_countries_and_cities

def populate_geo_data():
    init()

    parse_city()
    parse_country()

    remove_non_match_language_countries_and_cities()

    save_cities()
    save_countries()
