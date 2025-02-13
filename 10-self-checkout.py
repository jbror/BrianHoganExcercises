#10 Self-Checkout
import math #


def prompt_float(prompt):
    while True:
        try:
            pos = float(input(prompt))
            return pos
        except ValueError:
            print('Just floats')



item_count = 0
quantity    = 0
price      = 0

items = []


price_of_item = prompt_float(f'Enter price of item {str(item_count +1)}:\n')
quantity_of_item = prompt_float(f'Enter the quantity of item {str(item_count +1)}:\n')
item_count +=1


items.append({'item_number'+str(item_count):{'price':price_of_item}})
items[0]='item_number'+str(item_count)'quantity':= 2
print(items)


#item_and_price = # store in this? Dictonary maybe?










"""

square_feet = calculate_area(area_length, area_width) # Get the area of the room in square feet
gallons_needed_count = calculate_gallons_needed(square_feet) # Display the output

print(f'You will need to buy {gallons_needed_count} gallons of paint to cover {square_feet} square feet.')


"""
