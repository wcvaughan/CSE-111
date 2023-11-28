import math

no_items = int(input('Enter the number of items: '))

items_per_box = int(input('Enter the number of items in each box: '))

no_boxes = math.ceil(no_items / items_per_box)

print(f'For {no_items}, packing {items_per_box}, you will need {no_boxes}')