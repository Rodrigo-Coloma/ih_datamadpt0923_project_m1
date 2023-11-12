import pandas as pd
import requests


def interest_points(url):
    base_url = 'https://datos.madrid.es/egob'
    df = pd.json_normalize(requests.get(base_url + url).json()['@graph'])
    print('Interest points dataframe created')
    return df

def bicimad(path):
    df = pd.read_csv(path, sep='\t')
    df = df.reset_index(drop=True).loc[:,'name':]
    df.columns = ['BiciMAD station', 'light', 'number', 'Station location', 'activate','no_available', 'total_bases', 'dock_bikes', 'free_bases', 'reservations_count', 'geometry.type', 'geometry.coordinates']
    df[['longitude', 'latitude']] = df['geometry.coordinates'].str.strip('[]').str.split(',',expand= True).astype('float64')
    print('Bicimad dataframe created')
    return df
