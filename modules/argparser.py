import argparse

def args():
    parser = argparse.ArgumentParser(description= 'Application for BICImad localization' )
    help_all ='If you include this flag a dataframe with the nearest BiciMAD station will be added for each point of interest in the dataset' 
    parser.add_argument('-a', '--all', action='store_true', help=help_all)
    help_route ='This flag lets you create a custom route and generates a map with relevant information' 
    parser.add_argument('-r', '--route', action='store_true', help=help_route)
    help_start ='The location from wich yo want thee route to start' 
    parser.add_argument('-s', '--start', type=str, help=help_start)
    help_finish ='The location of the place you want the route to finish' 
    parser.add_argument('-f', '--finish', type=str, help=help_finish)
    help_places ='A string with all the monuments you want to visit separated by commas' 
    parser.add_argument('-p', '--places', type=str, help=help_places)
    help_email ='The email you want the information to be sent to'
    parser.add_argument('-e', '--email', type=str, help=help_email)
    args = parser.parse_args()
    return args
