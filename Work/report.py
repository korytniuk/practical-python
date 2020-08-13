# report.py
#
# Exercise 2.4
import csv
import tableformat
from stock import Stock
from fileparse import parse_csv
from portfolio import Portfolio

def print_report(report: list, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def read_portfolio(filename):
    with open(filename) as lines:
        portfolio = [Stock(r['name'],r['shares'],r['price']) for r in parse_csv(lines, types=[str,int,float])]

    return Portfolio(portfolio)

def read_prices(filename):
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str,float], has_headers=False))

def make_report_data(portfolio, prices):
    combined = []

    for x in portfolio:
        parsed = x.__dict__
        parsed['change'] = prices[x.name] - x.price
        combined.append(tuple(parsed.values())) 

    return combined

def portfolio_report(f1, f2, fmt='txt'):
    port = read_portfolio(f1)
    prices = read_prices(f2)
    combined = make_report_data(port, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(combined, formatter)


def main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    if len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        print(f'Invalid usage')
if __name__ == '__main__':
    from sys import argv
    main(argv)
