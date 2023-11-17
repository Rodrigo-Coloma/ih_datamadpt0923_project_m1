# import library
from modules.argparser import termArgs
import modules.dataframe_creation as dc
import modules.main_operations as mo
import modules.route_generator as rg
import modules.map_generator as mg
from datetime import datetime
import time
import os
start = time.time()

def main():
    
    #Inputs
    folder = str(datetime.now()).split('.')[0].replace(':', '').replace(' ','_')
    os.mkdir(f'./data/output/{folder}')
    start_stop = rg.start_end(rg.arg_parser(termArgs().route,termArgs().start,termArgs().finish))
    if termArgs().email:
        mail = input('Enter an email to send the route information :')

    #Pipeline
    places_df = dc.interest_points(start_stop)
    bicimad_df = dc.bicimad()
    all_places_df =mo.nearest(places_df, bicimad_df,folder)
    if termArgs().route:
        route_df = mo.route(all_places_df, folder,termArgs().places)
        stops_coordinates = rg.stations_coordinates(route_df,bicimad_df)
        optimized_coordinates = rg.route_optimizer(stops_coordinates)
        route_coordinates = rg.route_generator(optimized_coordinates)
        mg.mapGen(route_coordinates,optimized_coordinates,places_df,route_df,folder)
    elif not termArgs().all:
        mo.route(all_places_df, folder,termArgs().places)
    
# Pipeline execution 
if __name__ == '__main__':
    main()
    end = time.time()
    print(end - start)
# C:/Users/rjcol/miniconda3/envs/pm1/python.exe c:/Users/rjcol/ironhack/project/project_module_1/ih_datamadpt0923_project_m1/main.py -r -s "calle pez, 2" -f "Calle de tetuan" -p "fuente de cibeles, neptuno, Maestro alonso, La gloria y los pegasos, cabo naval, El vecino curioso"