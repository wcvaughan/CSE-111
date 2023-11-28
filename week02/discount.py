import math
from datetime import datetime

user_subtotal = float(input('What does the cost come to?'))

current_day = datetime.now()

day_of_the_week = current_day.weekday()

discount = 0

if user_subtotal >= 50:
    if day_of_the_week == 1 or 2:
        discount = user_subtotal * .1
        user_subtotal = user_subtotal - discount

sales_tax = user_subtotal * .06

total = user_subtotal + sales_tax


if day_of_the_week == 1 or 2:
    print(f'Thank you for shopping with us! Your total without tax is {user_subtotal:.2f} and sales tax is {sales_tax:.2f} AND your discount is {discount:.2f} if you spend more than $50 with us today you will receive a 10% off coupon from you total order! Your total is {total:.2f} ')
else:
    print(f'Your total without tax is {user_subtotal:.2f} and sales tax is {sales_tax:.2f}. Your total comes to {total}.')
