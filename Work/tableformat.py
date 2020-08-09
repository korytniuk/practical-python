# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in text-plain format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{str(d):>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Emit a table in csv format
    '''

    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Emit a table in html format
    '''
    def headings(self, headers):
        print(f'<tr>{"".join([f"<th>{h}</th>" for h in headers])}</tr>')
    
    def row(self, rowdata):
        print(f'<tr>{"".join([f"<td>{d}</td>" for d in rowdata])}</tr>')


def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    if fmt == 'csv':
        return CSVTableFormatter()
    if fmt == 'html':
        return HTMLTableFormatter()

    raise NotImplementedError() 

def print_table(data, columns, fmt):
    fmt.headings(columns) 
    for item in data:
        fmt.row(tuple([getattr(item, col) for col in columns]))