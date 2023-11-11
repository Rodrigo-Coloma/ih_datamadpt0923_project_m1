##############################################################################
#                                                                            #                       
#   argparse — Parser for command-line options, arguments and sub-commands   #     
#                                                                            #
#   Ironhack Data Part Time --> Sep-2023                                    #
#                                                                            #
##############################################################################


# import library

import argparse


# Script functions 

def enter_number(message):
    return float(input(message))

def sum_function(x1, x2):
    return x1 + x2
    
def multiply_function(x1, x2):
    return x1 * x2
    

# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Application for arithmetic calculations' )
    help_message ='You have two options. Option 1: "mult" performs multiplication of two given numbers. Option 2: "sum" performs the sum of two given numbers' 
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args


# Pipeline execution

if __name__ == '__main__':
    if argument_parser().function == 'mult':
        n1 = enter_number('Enter a number: ')
        n2 = enter_number('Enter another number: ')
        result = multiply_function(n1, n2)
    elif argument_parser().function == 'sum':
        n1 = enter_number('Enter a number: ')
        n2 = enter_number('Enter another number: ')
        result = sum_function(n1, n2)
    else:
        result = 'FATAL ERROR...you need to select the correct method'
    print(f'The result is => {result}')