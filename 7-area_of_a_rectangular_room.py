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



area_length = prompt_float('Howdy! What is the length of the room in feet? (I know that it\'s a sucky way to measure btw..!)\n')
area_width = prompt_float('And what is the width of the room in feet?\n')

square_feet = calculate_area(area_length, area_width)
square_meters = square_feet * 0.09290304

print('This is the square feet and square meters(rounded with 3 decimals!)')
print(square_feet, str('Square feet'))
print(round(square_meters,3),str('Square meters'))
