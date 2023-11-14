import folium
import matplotlib.image as mpimg
import webbrowser
import os


def mapGen(route, stops, interest, route_df, path):
    m = folium.Map(location=[stops[0][0], stops[0][1]], zoom_start=14)
    folium.PolyLine(route).add_to(m)
    icon_image = mpimg.imread('./data/origin/bicimad_icon.webp')
    lat_stops = [i[0] for i in stops]
    lon_stops = [i[1] for i in stops]
    for lat, lon, bikes, docks, name  in zip(lat_stops,lon_stops, route_df['Available bikes'], route_df['Available docks'], route_df['BiciMAD station']):
        icon = folium.CustomIcon(icon_image, icon_size=(28, 28))
        popup = folium.Popup(f'<h2"> BiciMAD station: {name} </h2><h5>Available bikes: {bikes}<br />Available docks : {docks}</h5>', min_width=300, max_width=300)
        folium.Marker(location=[lat, lon], icon=icon, popup=popup).add_to(m)
    target_df = interest.set_index('title').loc[list(route_df.index),]
    sw = target_df[['location.latitude', 'location.longitude']].min().values.tolist()
    ne = target_df[['location.latitude', 'location.longitude']].max().values.tolist()
    m.fit_bounds([[i - 0.002 for i in sw], [i + 0.002 for i in ne]])
    icon_image = mpimg.imread('./data/origin/monument_icon.png')
    for lat, lon, name, link in zip(target_df['location.latitude'], target_df['location.longitude'],target_df.index,target_df['relation']):
        icon = folium.CustomIcon(icon_image, icon_size=(48, 48))
        popup = folium.Popup(f'<h3 style="color: #5e9ca0;"><a href={link}>{name} </a></h3>', min_width=300, max_width=300)
        folium.Marker(location=[lat,lon], icon=icon, popup=popup).add_to(m)
    m.save(f'./data/output/{path}/route_map.html')
    webbrowser.open('file://' + os.path.realpath(f'./data/output/{path}/route_map.html'))