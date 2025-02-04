#Pizza Party!
def prompt_int(prompt_message):
    while True:
        try:
            prompt = int(input(prompt_message))
            return prompt
        except ValueError:
            print('Just numbers..')

def pizza_calculator(people, pizzas, slices=8):
    total_slices = pizzas * slices
    slices_per_person =  total_slices // people
    leftovers = total_slices % people
    return people, pizzas, slices, total_slices, slices_per_person, leftovers

def display_pizza_information(people, pizzas, slices, total_slices, slices_per_person, leftovers):
    print(f'Alright.. {people} people with {pizzas} pizzas sliced in {slices} slices per pizza')
    print(f'Total slices: {total_slices}')
    print(f'And all humans will get {slices_per_person} slices')
    print(f'Slice leftover count: {leftovers}')

number_of_humans = prompt_int('How many humans will eat?\n')
number_of_pizzas = prompt_int('And how many pizzas will you have and slay in your mouth?\n')
number_of_slices = prompt_int('Tell me how many slices you like per pizza. 8 is standard on planet earth\n')

pizza_data = pizza_calculator(number_of_humans,number_of_pizzas,number_of_slices)
display_pizza_information(*pizza_data)
