import pandas as pd
import requests
import modules.geo_calculations as gc

def interest_simplification(df):
    df['Type of place'] = 'Monument'
    df=df[['title', 'Type of place', 'address.street-address']]
    df.columns = ['Place of interest', 'Type of place', 'Place address']
    return df

def nearest(df1, df2, interest_point):
    try:
        i = [x.lower().split('- ')[-1] for x in df1['title']].index(interest_point.lower())
        lat, lon = df1['location.latitude'][i], df1['location.longitude'][i]
        dist = [gc.distance_meters(lat, lon, df2['latitude'][i], df2['longitude'][i])[0] for i in range(len(df2['longitude']))]
        nearest_station_df = df2.loc[dist.index(min(dist)),['BiciMAD station','Station location']]._append(pd.Series({'Distance to station (meters)' : round(min(dist),0)}))
        ps = interest_simplification(df1).iloc[i,:]._append(nearest_station_df)
        print(f'{interest_point} added to dataframe')
        return ps
    except IndexError:
        print(f'{interest_point} is not on the database')