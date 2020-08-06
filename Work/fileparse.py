# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select: list = [], types: list = [], has_headers=True, delimiter=',', silence_error=False) -> list:
    '''
    Parse a CSV file to a list of records
    '''
    
    if select and not has_headers:
        raise RuntimeError('select arguments requires column headers')

    records = []
    rows = csv.reader(lines)
    
    header = next(rows) if has_headers else []
    if select:
        indices = [ header.index(x) for x in select]
        header = select

    for row in rows:
        if not row:
            continue

        if select:
            row = [ row[index] for index in indices ]

        try:
            if types:
                row = [ func(val) for func, val in zip(types, row) ]

            if has_headers:
                record = dict(zip(header, row)) 
            else:
                record = tuple([k for k in row ])

            records.append(record)
        except ValueError as e:
            if not silence_error:
                print(f'The record can\'t be created for: {row}')
                print(f'Error: {e}')


    return records 

