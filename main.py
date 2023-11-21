from modules.argparser import termArgs
import modules.dataframe_creation as dc
import modules.main_operations as mo
import modules.route_generator as rg
import modules.map_generator as mg
from modules.email_generator import email

def main():
    
    places_df = dc.interest_points(termArgs())
    bicimad_df = dc.bicimad()
    all_places_df =mo.nearest(places_df, bicimad_df)
    if termArgs().route:
        target_df = mo.target(all_places_df,termArgs().places,termArgs().route)
        stops_coordinates = rg.stations_coordinates(target_df,bicimad_df)
        optimized_coordinates = rg.route_optimizer(stops_coordinates)
        route_coordinates = rg.route_generator(optimized_coordinates)
        mg.mapGen(route_coordinates,optimized_coordinates,places_df,target_df)
    elif not termArgs().all:
        mo.target(all_places_df,termArgs().places,termArgs().route)
    email(termArgs().email)
     
if __name__ == '__main__':
    main()

#C:/Users/rjcol/miniconda3/envs/pm1/python.exe c:/Users/rjcol/ironhack/project/project_module_1/ih_datamadpt0923_project_m1/main.py -r -s "calle pez, 2" -f "Calle de tetuan" -p "fuente de cibeles, neptuno, Maestro alonso, La gloria y los pegasos, cabo naval, El vecino curioso" -e "rjcolgut@gmail.com"