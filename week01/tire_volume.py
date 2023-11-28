import math

"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = (math.pi * (w ** 2) * a * (w * a + 2450 * d)) / 10000000000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

"""

print('I can calculate the volume of your tire!')

width = int(input('Enter the width of the tire in mm (ex 205): '))

aspect = int(input('Enter the aspect ratio of the tire (ex 60): '))

diameter = int(input('Enter the diameter of the tire in inches (ex 15): '))

volume = (math.pi * (width ** 2) * aspect * ((width * aspect) + (2450 * diameter))) / 10000000000

print(f'The approximate volume is: {volume:.2f}')