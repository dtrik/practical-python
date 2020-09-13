# mortgage.py
#
# Exercise 1.7
principal = 500000
interest = 0.05
monthly = 2684.11
paid = 0
month = 0
while principal > 0:
    month += 1
    principal = principal * (1 + interest/12) - (monthly+1000*(month<=12))
    paid += monthly+(1000*(month<=12))

print('Total paid', paid, 'in', month)
