import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('podstawa', type=int,
                    help='an integer for the accumulator')

parser.add_argument('wykladnik', type=int,
                    help='an integer for the accumulator')

args = parser.parse_args()

print(args)
print(args.podstawa)
print(args.wykladnik)
wynik = pow(args.podstawa, args.wykladnik)
print("Wynik " + str(wynik))

