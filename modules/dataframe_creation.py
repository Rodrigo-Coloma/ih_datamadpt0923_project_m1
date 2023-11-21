import pandas as pd
import requests
from dotenv import dotenv_values
from modules.route_generator import arg_parser, start_end


def interest_points(args):
    print(args)
    base_url = 'https://datos.madrid.es/egob'
    url = '/catalogo/300356-0-monumentos-ciudad-madrid.json'
    df = pd.json_normalize(requests.get(base_url + url).json()['@graph'])
    if args.route and args.start and args.finish:
        route = start_end(arg_parser(args.route,args.start,args.finish))
        if route:
            start= pd.Series({'@id':'', 'id':'', 'title':'Starting location', 'relation':'', 'references':'', 'address.district.@id':'',
            'address.locality':'', 'address.postal-code':'', 'address.street-address':route[0],
            'location.latitude': float(route[1][0]), 'location.longitude': float(route[1][1]),
            'organization.organization-desc':'', 'organization.organization-name':'',
            'address.area.@id':''})
            stop= pd.Series({'@id':'', 'id':'', 'title':'Finish location', 'relation':'', 'references':'', 'address.district.@id':'',
            'address.locality':'', 'address.postal-code':'', 'address.street-address':route[2],
            'location.latitude': float(route[3][0]), 'location.longitude': float(route[3][1]),
            'organization.organization-desc':'', 'organization.organization-name':'',
            'address.area.@id':''})
            df = pd.concat([start.to_frame().T,df,stop.to_frame().T], axis=0).reset_index(drop=True)        
            df[['location.latitude','location.longitude']] = df[['location.latitude','location.longitude']].astype(float)
    print('Interest points dataframe created')
    return df

def bicimad():
    emt_email = dotenv_values('./.env')['EMT_EMAIL']
    emt_password = dotenv_values('./.env')['EMT_PASSWORD']
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
