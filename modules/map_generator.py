import folium
import matplotlib.image as mpimg
import webbrowser
import os
from dotenv import dotenv_values
import requests
import pandas as pd

def nearby(lat,lon,type):
  places_url = 'https://places.googleapis.com/v1/places:searchNearby'
  token_gmap = dotenv_values('./.env')['CLAVE_GMAP']
  data={"includedTypes": [type],
    "maxResultCount": 10,
    "locationRestriction": {
      "circle": {
        "center": {
          "latitude": lat,
          "longitude": lon},
        "radius": 250.0
      }
    }
  }
  places_headers = {'Content-Type': 'application/json','X-Goog-Api-Key':f'{token_gmap}','X-Goog-FieldMask': '*'}
  return pd.json_normalize(requests.post(places_url,headers=places_headers,json=data).json()['places'])



def mapGen(route, stops, interest, route_df, path):
    m = folium.Map(location=[stops[0][0], stops[0][1]], zoom_start=14)
    folium.PolyLine(route).add_to(m)
    lat_stops = [i[0] for i in stops]
    lon_stops = [i[1] for i in stops]
    for lat, lon, bikes, docks, name  in zip(lat_stops,lon_stops, route_df['Available bikes'], route_df['Available docks'], route_df['BiciMAD station']):
        icon_image = mpimg.imread('./data/origin/bicimad_icon.webp')
        icon = folium.CustomIcon(icon_image, icon_size=(28, 28))
        popup = folium.Popup(f'<h3> BiciMAD station: {name} </a></h3><h5>Available bikes: {bikes}<br />Available docks : {docks}</h5>', min_width=300, max_width=300)
        folium.Marker(location=[lat, lon], icon=icon, popup=popup).add_to(m)
        try:
            places = nearby(lat,lon,'tourist_attraction')
            try:
                places['websiteUri'] = places['websiteUri'].fillna('')
            except:
                places['websiteUri'] = ''
            icon_image = mpimg.imread('./data/origin/camera_icon.png')
            for lat, lon, uri, name, type in zip(places['location.latitude'], places['location.longitude'], places['websiteUri'], places['displayName.text'],places['primaryTypeDisplayName.text']):
                icon = folium.CustomIcon(icon_image, icon_size=(28, 28))
                popup = folium.Popup(f'<h3><a href={uri}>{name} </a></h3><h4>{type}</h4>', min_width=300, max_width=300)
                folium.Marker(location=[lat,lon], icon=icon, popup=popup).add_to(m)
        except:
            pass
        try:
            restaurants = nearby(lat,lon,'restaurant')
            try:
                restaurants['websiteUri'] = restaurants['websiteUri'].fillna('')
            except:
                restaurants['websiteUri'] = ''
            icon_image = mpimg.imread('./data/origin/restaurant_icon.png')
            for lat, lon, uri, name, type, rating, votes in zip(restaurants['location.latitude'], restaurants['location.longitude'], restaurants['websiteUri'], restaurants['displayName.text'],restaurants['primaryTypeDisplayName.text'],restaurants['rating'],restaurants['userRatingCount']):
                icon = folium.CustomIcon(icon_image, icon_size=(28, 28))
                popup = folium.Popup(f'<h3><a href={uri}>{name} </a></h3><h4>{type}<br>Rating: {rating}/5 ({votes} votes)</h4>', min_width=300, max_width=300)
                folium.Marker(location=[lat,lon], icon=icon, popup=popup).add_to(m)
        except:
            pass
    target_df = interest.set_index('title').loc[list(route_df.index),]
    sw = target_df[['location.latitude', 'location.longitude']].min().values.tolist()
    ne = target_df[['location.latitude', 'location.longitude']].max().values.tolist()
    m.fit_bounds([[i - 0.002 for i in sw], [i + 0.002 for i in ne]])
    icon_image = mpimg.imread('./data/origin/start_icon.png')
    icon = folium.CustomIcon(icon_image, icon_size=(48, 48))
    popup = folium.Popup(f'<h3 style="color: #5e9ca0;">{target_df.index[0]} </a></h3>', min_width=300, max_width=300)
    folium.Marker(location=[target_df['location.latitude'][0],target_df['location.longitude'][0]], icon=icon, popup=popup).add_to(m)
    icon_image = mpimg.imread('./data/origin/monument_icon.png')
    for lat, lon, name, link in zip(target_df['location.latitude'][1:-1], target_df['location.longitude'][1:-1],target_df.index[1:-1],target_df['relation'][1:-1]):
        icon = folium.CustomIcon(icon_image, icon_size=(48, 48))
        popup = folium.Popup(f'<h3 style="color: #5e9ca0;"><a href={link}>{name} </a></h3>', min_width=300, max_width=300)
        folium.Marker(location=[lat,lon], icon=icon, popup=popup).add_to(m)
    icon_image = mpimg.imread('./data/origin/stop_icon.png')
    icon = folium.CustomIcon(icon_image, icon_size=(48, 48))
    popup = folium.Popup(f'<h3 style="color: #5e9ca0;">{target_df.index[-1]} </a></h3>', min_width=300, max_width=300)
    folium.Marker(location=[target_df['location.latitude'][-1],target_df['location.longitude'][-1]], icon=icon, popup=popup).add_to(m)
    icon_image = mpimg.imread('./data/origin/monument_icon.png')
    m.save(f'./data/output/{path}/route_map.html')
    webbrowser.open('file://' + os.path.realpath(f'./data/output/{path}/route_map.html'))