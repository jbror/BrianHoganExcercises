print('yo')
#draft atm...!

def prompt_length_width_in_feet(prompt):
    while True:
        try:
            area_data = float(input(prompt))
            return area_data
        except ValueError:
            print('Just floats')




length_feet = prompt_length_width_in_feet('Howdy! What is the length of the room in feet? (I know that it\'s a sucky way to measure btw..!)\n')
width_feet = prompt_length_width_in_feet('And what is the width of the room in feet?\n')
