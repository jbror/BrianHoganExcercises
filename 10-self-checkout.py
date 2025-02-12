#10 Self-Checkout
import math # to use the Python math.ceil() method

PAINT_COVERAGE = 350 # 1 gallon per 350 square feet

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


area_length = prompt_float('Howdy! What is the length of the room in feet? (I know that it\'s a sucky way to measure btw..!)\n')
area_width = prompt_float('And what is the width of the room in feet?\n')
square_feet = calculate_area(area_length, area_width) # Get the area of the room in square feet
gallons_needed_count = calculate_gallons_needed(square_feet) # Display the output

print(f'You will need to buy {gallons_needed_count} gallons of paint to cover {square_feet} square feet.')


# Write your code here :-)
