
# Ask for input and count the numbers of characters of the given input. Output; Display the given string input plus the numbers
# of characters.
# Example: Enter string: Cake
# Cake has for characters.

#Input = promptUserForInput()
#Display (input + "contains" input.length + "characters")
# if input == blank
#   prompt for valid input. "No blank input"
#
# End


def count_characters_of_input():
    prompt = input('Hi buddy. Please give me some input so i can show my magic!\n')
    while True:
        len_input = len(prompt)
        if len_input == 0:
            print('No blank input! Give me something more. ',end='')
            prompt = input('Try again..\n')
        else:
            break
    print(prompt + ' contains ' + str(len_input) + ' characters')

count_characters_of_input()
