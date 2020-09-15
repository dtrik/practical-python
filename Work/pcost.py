# pcost.py
#
# Exercise 1.27
import csv
def portfolio_cost(filename):
    '''Returns the total cost of the portfolio in file
    passed as input to the function'''
    total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            #item = line.split(',')
            try:
                num_stock = int(row[1])
                cost_stock = float(row[2])
                total_cost += num_stock*cost_stock
            except ValueError:
                print(f'Skipping missing entry in {line}')
                continue
            #print(f'Total cost {total_cost}')
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')
