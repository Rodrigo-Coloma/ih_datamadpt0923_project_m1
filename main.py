# import library
import modules.dataset_creation as dc
import modules.main_operations as mo
import modules.geo_calculations as gc
import pandas as pd
import argparse
  

# Argument parser function

def terminal_input():
    parser = argparse.ArgumentParser(description= 'Application for BICImad localization' )
    help_all ='If you include this flag a dataframe with the nearest BiciMAD station will be added for eaach pint of interest in the dataset' 
    parser.add_argument('-a', '--all', action='store_true', help=help_all)
    help_name = ''
    parser.add_argument('-n','--name', action='store_true', help=help_name)
    args = parser.parse_args()
    return args

def main():

    # Inputs

    interest_url = '/catalogo/300356-0-monumentos-ciudad-madrid.json'
    bicimad_path = './data/origin/bicimad_stations.csv'
    bicipark_path = './data/origin/bicipark_stations.csv' 
    places = ['Abstracta II']
    
    #Pipeline

    interest_point_df = dc.interest_points(interest_url)
    bicimad_df = dc.bicimad(bicimad_path)
    if terminal_input().all:
        places = interest_point_df['title']
    elif terminal_input().name:
        places = [x.strip() for x in input('Enter the name/names of the monuments you are visiting separated by commas: ').split(',')]         
    nearest_df = pd.concat([mo.nearest(interest_point_df,bicimad_df, place) for place in places],axis=1)
    nearest_df.to_csv('./data/output/'+ '1_all_' * terminal_input().all + 'nearest_stations.csv')

# Pipeline execution

if __name__ == '__main__':
    main()