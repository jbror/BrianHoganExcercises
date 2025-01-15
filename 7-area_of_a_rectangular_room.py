print('yo')
#draft atm...!

def prompt_length_width(prompt):
    while True:
        try:
            area_data = float(input(prompt))
            return area_data
        except ValueError:
            print('Just floats')


def calculate_area(length, width):
    square_unit = length * width

    square_feet = round(square_unit)
    square_meters = square_unit * 0.09290304

    rounded_square_meters = round(square_meters, 3)


    print(square_feet)
    print(rounded_square_meters)


length_feet = prompt_length_width('Howdy! What is the length of the room in feet? (I know that it\'s a sucky way to measure btw..!)\n')
width_feet = prompt_length_width('And what is the width of the room in feet?\n')


calculate_area(length_feet, width_feet)
