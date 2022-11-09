import argparse
import math
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('zakres', type=int,
                    help='an integer for the accumulator')

args = parser.parse_args()

wynik = args.zakres/ math.log(args.zakres)

while True :
    print("")
    user_input = input ("Wpisz zakres: ")
    if user_input != "x":
        print("Ok, wynik to " + str(int(wynik)))
    elif user_input == "x":
        print("sayonnara")
        exit()
    
