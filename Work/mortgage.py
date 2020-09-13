# mortgage.py
#
# Exercise 1.7
principal = 500000
interest = 0.05
monthly = 2684.11
paid = 0

while principal > 0:
    principal = principal * (1 + interest/12) - monthly
    paid += monthly

print('Total paid', paid)
