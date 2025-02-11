#Paint Calculator




def prompt_int(prompt_message):
    while True:
        try:
            prompt = int(input(prompt_message))
            return prompt
        except ValueError:
            print('Just numbers..')




ceiling_length = prompt_int('Tell me the length of the ceiling\n')
ceiling_width = prompt_int('Tell me the width of the ceiling\n')
