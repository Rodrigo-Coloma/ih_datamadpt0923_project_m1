import requests
from dotenv import dotenv_values
from polyline import decode
from modules.argparser import termArgs

def stations_coordinates(df1,df2):
    stations = list(df1['BiciMAD station'])
    latitudes = [df2.loc[df2['BiciMAD station'] == station,['latitude']].iloc[0,0] for station in stations]
    longitudes = [df2.loc[df2['BiciMAD station'] == station,['longitude']].iloc[0,0] for station in stations]
    return list(zip(latitudes,longitudes))

def start_end(start_end):
  route_url = 'https://routes.googleapis.com/directions/v2:computeRoutes' 
  token_gmap = dotenv_values('./.env')['CLAVE_GMAP']

  data={"origin":{ "address": start_end[0]}, 
    "destination":{ "address": start_end[1]},
    "travelMode": "TRANSIT",
    "languageCode": "en-US",
    "units": "IMPERIAL"
  }
  headers = {'Content-Type': 'application/json','X-Goog-Api-Key':f'{token_gmap}','X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'}

  response = requests.post(route_url, headers=headers, json=data)
  if response.status_code == 200:
    coordinates = decode(response.json()['routes'][0]['polyline']['encodedPolyline'])
    return [start_end[0]] + [coordinates[0]] + [start_end[1]] + [coordinates[-1]]
  else:
    print('Addresses for starting or finishing weren not valid')
    return False

def arg_parser(route,start,end):
  if route:
    if not start:
      start = input("Enter the address for your rout's starting point: ")
    if not end:
      start = input("Enter the address for your rout's finishing point: ")
    return (start, end)

def route_optimizer(coordinates):
  if len(coordinates) > 3:
    route_url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
    token_gmap = dotenv_values('./.env')['CLAVE_GMAP'] 
  
    data={"origin":{
        "location":{
        "latLng":{
          "latitude": coordinates[0][0],
          "longitude": coordinates[0][1]
        }
      }
    },
    "destination":{
      "location":{
        "latLng":{
          "latitude": coordinates[-1][0],
          "longitude": coordinates[-1][1]
        }
      }
    },
    "optimizeWaypointOrder": "true",
    "travelMode": "DRIVE",
    "languageCode": "en-US",
    "units": "IMPERIAL"
    } 
    data['intermediates'] = [{'location':{'latLng':{'latitude': coordinates[i][0],'longitude': coordinates[i][1]}}} for i in range(1,len(coordinates)-1)]
    headers = {'Content-Type': 'application/json','X-Goog-Api-Key':f'{token_gmap}','X-Goog-FieldMask': 'routes.optimizedIntermediateWaypointIndex'}

    response = requests.post(route_url, headers=headers, json=data)
    indexes = [i+1 for i in response.json()['routes'][0]['optimizedIntermediateWaypointIndex']]
    return [coordinates[0]] + [coordinates[i] for i in indexes] + [coordinates[-1]]
  else:
    return coordinates
  

def section_generator(start,end):
  route_url = 'https://routes.googleapis.com/directions/v2:computeRoutes' 
  token_gmap = dotenv_values('./.env')['CLAVE_GMAP']

  data={"origin":{
      "location":{
        "latLng":{
          "latitude": start[0],
          "longitude": start[1]
        }
      }
    },
    "destination":{
      "location":{
        "latLng":{
          "latitude": end[0],
          "longitude": end[1]
        }
      }
    },
    "travelMode": "BICYCLE",
    "languageCode": "en-US",
    "units": "IMPERIAL"
  }
  headers = {'Content-Type': 'application/json','X-Goog-Api-Key':f'{token_gmap}','X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'}

  response = requests.post(route_url, headers=headers, json=data)
  return decode(response.json()['routes'][0]['polyline']['encodedPolyline'])

def route_generator(stop_coordinates):
  route_coordinates = []
  for i in range(len(stop_coordinates)-1):
    route_coordinates += section_generator(stop_coordinates[i],stop_coordinates[i+1])
  return route_coordinates