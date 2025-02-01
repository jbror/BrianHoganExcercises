#Pizza Party!

def prompt_int(prompt_message):
    while True:
        try:
            prompt = int(input(prompt_message))
            return prompt
        except ValueError:
            print('Just numbers..')



def pizza_calculator(people,pizzas,slices):
    total_slices = pizzas * slices
    slices_per_person =  total_slices // people
    leftovers = total_slices % people
    #just testing below!
    print(f'You are {number_of_humans} humans in this room')
    print('Total slices:',total_slices)
    print('And all humans will get:', slices_per_person)
    print('Leftover slices:', leftovers)






number_of_humans = prompt_int('How many humans will eat?')
number_of_pizzas = prompt_int('And how many pizzas will you have and slay in your mouth?')
number_of_slices = prompt_int('Tell me how many slices you like per pizza!')

info = pizza_calculator(number_of_humans,number_of_pizzas,number_of_slices)
