from modules.argparser import args
import modules.dataframe_creation as dc
import modules.main_operations as mo
import modules.route_generator as rg
import modules.map_generator as mg
from modules.email_generator import email

def main():
    
    places_df = dc.interest_points(args())
    bicimad_df = dc.bicimad()
    all_places_df =mo.nearest(places_df, bicimad_df)
    if not args().all:
        target_df = mo.target(all_places_df,args().places,args().route)
    if args().route:
        stops_coordinates = rg.stations_coordinates(target_df,bicimad_df)
        optimized_coordinates = rg.route_optimizer(stops_coordinates)
        route_coordinates = rg.route_generator(optimized_coordinates)
        mg.mapGen(route_coordinates,optimized_coordinates,places_df,target_df)
    email(args().email)
     
if __name__ == '__main__':
    main()

#C:/Users/rjcol/miniconda3/envs/pm1/python.exe c:/Users/rjcol/ironhack/project/project_module_1/ih_datamadpt0923_project_m1/main.py -r -s "Plaza de Callao" -f "Plaza de España" -p "fuente de cibeles, neptuno, Maestro alonso, La gloria y los pegasos, cabo naval, El vecino curioso" -e "rjcolgut@gmail.com"