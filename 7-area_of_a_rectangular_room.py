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
    square_meters = round(square_unit * 0.09290304, 3)
    return square_feet, square_meters




length_feet = prompt_length_width('Howdy! What is the length of the room in feet? (I know that it\'s a sucky way to measure btw..!)\n')
width_feet = prompt_length_width('And what is the width of the room in feet?\n')
calc_area = calculate_area(length_feet, width_feet) # Should/could i name the var the same-ish as the func :P?
display_output_feet, display_output_meters = calc_area

print(display_output_feet)
print(display_output_meters)
