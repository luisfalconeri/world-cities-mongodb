import os

def get_data_folder_path():
    return os.path.join('modules/app_src/utils/world_cities_mongodb/data')

def get_country_data_path():
    return os.path.join(get_data_folder_path(), 'countryInfo.txt')

def get_city_data_path():
    return os.path.join(get_data_folder_path(), 'cities15000.txt')
