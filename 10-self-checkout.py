#10 Self-Checkout
import math #


def prompt_float(prompt):
    while True:
        try:
            area_data = float(input(prompt))
            return area_data
        except ValueError:
            print('Just floats')


def calculate_area(length, width):
    area = length * width
    return area


def calculate_gallons_needed(area): # How many whole gallons is needed? Find out with this!
    return math.ceil(area / PAINT_COVERAGE) # Rounds up to next whole number!


price_of_item = prompt_float('Enter price of item 1:\n')
quanity_of_item = prompt_float('Enter the quanity of item 1:\n')

item_and_price = # store in this? Dictonary maybe?




"""

square_feet = calculate_area(area_length, area_width) # Get the area of the room in square feet
gallons_needed_count = calculate_gallons_needed(square_feet) # Display the output

print(f'You will need to buy {gallons_needed_count} gallons of paint to cover {square_feet} square feet.')


"""
