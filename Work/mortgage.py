# mortgage.py
#
# Exercise 1.7
principal = 500000
interest = 0.05
monthly = 2684.11
paid = 0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    per_month = monthly+extra_payment*(month in range(
        extra_payment_start_month, 
        extra_payment_end_month+1))
    principal = principal * (1 + interest/12) - per_month
    paid += per_month
print('Total paid', paid, 'in', month)
