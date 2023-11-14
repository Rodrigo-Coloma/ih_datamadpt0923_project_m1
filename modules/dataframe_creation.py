import pandas as pd
import requests
from dotenv import dotenv_values

emt_email = dotenv_values('./.env')['EMT_EMAIL']
emt_password = dotenv_values('./.env')['EMT_PASSWORD']

def interest_points():
    base_url = 'https://datos.madrid.es/egob'
    url = '/catalogo/300356-0-monumentos-ciudad-madrid.json'
    df = pd.json_normalize(requests.get(base_url + url).json()['@graph'])
    print('Interest points dataframe created')
    return df

def bicimad():
    login_url = 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/'
    login_headers = {'email': emt_email, 'password': emt_password}
    login_response = requests.get(login_url,headers=login_headers)
    token = login_response.json()['data'][0]['accessToken']
    bicimad_headers = {'accessToken': token}
    bicimad_url = 'https://openapi.emtmadrid.es/v1/transport/bicimad/stations/'
    bicimad_response = requests.get(bicimad_url, headers=bicimad_headers)
    df = pd.json_normalize(bicimad_response.json()['data'])
    df.columns = ['activate', 'Station location', 'Available bikes', 'Available docks', 'id', 'light','BiciMAD station', 'no_available', 'number', 'reservations_count', 'total_bases', 'virtualDelete', 'geofenced_capacity', 'geometry.type', 'geometry.coordinates']
    df['longitude'] = df['geometry.coordinates'].apply(lambda x: x[0]).astype('float64')
    df['latitude'] = df['geometry.coordinates'].apply(lambda x: x[1]).astype('float64')
    df['BiciMAD station'] = [station.split('- ')[-1] for station in df['BiciMAD station']]
    print('Bicimad dataframe created')
    return df
