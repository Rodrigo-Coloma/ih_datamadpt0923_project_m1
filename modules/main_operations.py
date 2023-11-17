import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from IPython.display import display
from datetime import datetime

def interest_simplification(df):
    df['Type of place'] = 'Monument'
    df=df[['title', 'Type of place', 'address.street-address']]
    df.columns = ['Place of interest', 'Type of place', 'Place address']
    return df

def fuzzy_check(str,places):
    fuzzy_choice = process.extractOne(str, places, scorer=fuzz.token_sort_ratio)
    if fuzzy_choice[1] > 80:
        return fuzzy_choice[0]
    else:
        print(f"{str} doesn't match any monument in the database")

def nearest(places, bicimad,folder):
    bicimad = bicimad.loc[bicimad['Available bikes']>0,:]
    data_list = []
    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    bicimad_lat_rad = np.radians(bicimad['latitude'].to_numpy())
    bicimad_lon_rad = np.radians(bicimad['longitude'].to_numpy())
    dlat = bicimad_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_lon_rad[:, np.newaxis] - places_lon_rad
    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    """ Creación del dataframe del resultado utilizando ese índice"""

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = bicimad['BiciMAD station'].iloc[station_index].split('- ')[-1]
        station_address = bicimad["Station location"].iloc[station_index]
        type_of_place = 'Monument'
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        available_bikes = bicimad['Available bikes'].iloc[station_index]
        available_docks = bicimad['Available docks'].iloc[station_index]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"Place of interest": place,'Type of place': type_of_place, "Place address": place_address, "BiciMAD station": station, "Station location": station_address, 'Available bikes': available_bikes, 'Available docks': available_docks, "distance": min_distance})
    df = pd.DataFrame(data_list).set_index('Place of interest')
    df.iloc[1:-1,:].to_csv(f'./data/output/{folder}/1_all_nearest_stations.csv')
    return df
    
def route(df,path,places):
    start = True
    if not places:
        while start:
            places = input("Write the places you want to visit separated by comas: ").split(',')
            target_places = [fuzzy_check(place,df.index) for place in places]
            target_places = [place for place in target_places if place != None]
            if len(target_places)> 0:
                start = False
            else:
                print('Please, enter at least 1 valid location')
    else:
        target_places = [fuzzy_check(place,df.index) for place in places.split(',')]
        target_places = [place for place in target_places if place != None]
        if len(target_places) < 1:
            print('Please, enter at least 1 valid location')
    target_places = [df.index[0]] + target_places + [df.index[-1]]
    df = df.loc[target_places,:]
    df.to_csv(f'./data/output/{path}/nearest_stations_database.csv')
    display(df)
    return df