# pcost.py
#
# Exercise 1.27
import csv 
from fileparse import parse_csv

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"
    with open(filename) as f:
        records = parse_csv(f, types=[str,int,float])
        cost = sum([x['shares'] * x['price'] for x in records])
        print(f'Total cost {cost:0.2f}')

if __name__ == '__main__':
    from sys import argv
    main(argv)
    