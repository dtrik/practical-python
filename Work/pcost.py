# pcost.py
#
# Exercise 1.27
total_cost = 0
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        item = line.split(',')
        num_stock = int(item[1])
        cost_stock = float(item[2].strip('\n'))
        total_cost += num_stock*cost_stock
print(f'Total cost {total_cost}')
