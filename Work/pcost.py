# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    '''Returns the total cost of the portfolio in file
    passed as input to the function'''
    total_cost = 0
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            item = line.split(',')
            num_stock = int(item[1])
            cost_stock = float(item[2].strip('\n'))
            total_cost += num_stock*cost_stock

            #print(f'Total cost {total_cost}')
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')
