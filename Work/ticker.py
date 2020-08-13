# ticker.py

from follow import follow
from report import read_portfolio
from tableformat import create_formatter, print_table
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(port, stream, fmt):
    port = read_portfolio(port)
    rows = parse_stock_data(follow(stream))
    fmt = create_formatter(fmt)
    rows = filter_symbols(rows, port)

    fmt.headings(['Name', 'Price', 'Change']) 
    for row in rows:
        fmt.row(tuple(row.values()))

def filter_symbols(rows, symbols):
    return (row for row in rows if row['name'] in symbols)

def make_dicts(rows, keys):
    return (dict(zip(keys, row)) for row in rows)

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def select_columns(rows, indices):
    for row in rows:
       yield [row[index] for index in indices] 

if __name__ == '__main__':
    data = follow('Data/stocklog.csv')
    rows = parse_stock_data(data)
    for row in rows:
        print(row)
