# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv


def print_report(report: list):
    '''
    Print report
    '''

    if len(report) == 0:
        return 

    keys = report[0].keys()
    delimiter = ' '.join([f'{"_"*10}' for key in keys])
    header =  ' '.join([f'{key.capitalize():>10s}' for key in keys])

    print(header, '\n', delimiter)
    for row in report:
        print(' '.join([f'{str(x):>10s}' for x in row.values()]))


def combine(report, prices):
    prices = dict(prices)
    for x in report:
        change= x['price'] - prices[x['name']]
        x['change'] = f'{change:0.2f}'

    return report 


def portfolio_report(f1: str, f2: str):
    '''
    Read portfolio and pirces and print them
    '''
    print_report(combine(parse_csv(f1, types=[str,int,float]), parse_csv(f2, types=[str,float], has_headers=False)))

def main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    else:
        print(f'Invalid usage')
if __name__ == '__main__':
    from sys import argv
    main(argv)
