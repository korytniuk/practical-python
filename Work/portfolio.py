# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings
    
    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(name == p.name for p in self._holdings)
    
    @property
    def total_cost(self):
        return sum(x.cost for x in self._holdings)
    
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for row in self._holdings:
            total_shares[row.name] += row.shares
    
    def __iter__(self):
        return self._holdings.__iter__()