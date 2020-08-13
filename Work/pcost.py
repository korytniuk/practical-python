# pcost.py
#
# Exercise 1.27
import csv 
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"
    with open(filename) as f:
        records = [Stock(x['name'], x['shares'], x['price']) for x in parse_csv(f, types=[str,int,float])]
        portfolio = Portfolio(records)
        print(f'Total cost {portfolio.total_cost:0.2f}')

if __name__ == '__main__':
    from sys import argv
    main(argv)
    