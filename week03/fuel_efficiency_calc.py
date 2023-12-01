"""
Write a Python program that asks the user for three numbers:

A starting odometer value in miles

An ending odometer value in miles

An amount of fuel in gallons

Your program must calculate and print fuel efficiency in both miles per gallon

and liters per 100 kilometers. Your program must have three functions named as follows:

main

miles_per_gallon

lp100k_from_mpg

All user input and printing must be in the main function. In other words, the miles_per_gallon

and lp100k_from_mpg functions must not call the the input or print functions.

"""

def main():

    odometer_start = int(input('Please enter your starting odometer.'))

    odometer_end = int(input('Please enter your ending odometer.'))

    fuel_amount = float(input('How many gallons did you use?'))

    mpg = miles_per_gallon(odometer_start, odometer_end, fuel_amount)

    lp100k = lp100k_from_mph(mpg)

    print(f'Your fuel efficiency for now is {mpg:.2f} miles per gallon and if you are not in one of the few countries using imperial units, your fuel efficiency is {lp100k:.2f} liters per 100 kilometers')

def miles_per_gallon(odometer_start, odometer_end, gallons):

    mpg = float((odometer_end - odometer_start) / gallons)

    return mpg

def lp100k_from_mph(mpg):

    lp100k = 235.215 / mpg

    return lp100k

main()