# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment = 1000
extra_payment_start_month = 61
extra_paymnet_end_month = 108

month = 0

while principal > 0:
    month += 1
    total_payment = payment
    if month >= extra_payment_start_month and month <= extra_paymnet_end_month:
        total_payment += extra_payment

    principal = principal * (1+rate/12) - total_payment

    if principal < 0:
        total_payment += principal
        principal = 0
    
    total_paid = total_paid + total_payment
    print(f'{month}, {total_paid:0.2f}, {total_payment:0.2f}')
    
print(f'Total paid {total_paid:0.2f}')
print(f'Month {month}')