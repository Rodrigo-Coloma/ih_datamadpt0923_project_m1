# import library
import modules.dataframe_creation as dc
import modules.main_operations as mo
import modules.route_generator as rg
import modules.map_generator as mg
from datetime import datetime
import argparse
import time
import os
start = time.time()

# Argument parser function

def terminal_input():
    parser = argparse.ArgumentParser(description= 'Application for BICImad localization' )
    help_all ='If you include this flag a dataframe with the nearest BiciMAD station will be added for each point of interest in the dataset' 
    parser.add_argument('-a', '--all', action='store_true', help=help_all)
    help_route ='This flag lets you create a custom route and generates a map with relevant information' 
    parser.add_argument('-r', '--route', action='store_true', help=help_route)
    help_email ='This flag lets will send the generated information into the given mail'
    parser.add_argument('-e', '--email', action='store_true', help=help_email)
    args = parser.parse_args()
    return args

def main():
    
    #Inputs

    output_folder = str(datetime.now()).split('.')[0].replace(':', '').replace(' ','_')
    os.mkdir(f'./data/output/{output_folder}')
    if terminal_input().email:
        mail = input('Enter an email to send the route information :')

    #Pipeline

    interest_points_df = dc.interest_points()
    bicimad_df = dc.bicimad()
    all_places_df =mo.nearest(interest_points_df, bicimad_df)
    if terminal_input().route:
        route_df = mo.route(all_places_df, output_folder, terminal_input().route)
        stops_coordinates = rg.stations_coordinates(route_df,bicimad_df)
        if len(stops_coordinates) > 3:
            optimized_stop_coordinates = rg.route_optimizer(stops_coordinates)
        else:
            optimized_stop_coordinates = stops_coordinates
        route_coordinates = rg.route_generator(optimized_stop_coordinates)
        mg.mapGen(route_coordinates,optimized_stop_coordinates,interest_points_df,route_df,output_folder)

    elif not terminal_input().all:
        mo.route(all_places_df, output_folder)
    

# Pipeline execution 

if __name__ == '__main__':
    main()
    end = time.time()
    print(end - start)
# Example input: puerta alcala, dnoec, fuente cibeles, Abstracta