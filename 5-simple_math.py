def prompt_input():
    while True:
        try:
            first_num = float(input('Hi! Give me number '))
            second_num = float(input('I need a number again, pls! '))
            return first_num, second_num
        except ValueError:
            print('Only numbers!')
def sums(n1, n2):
    return n1 + n2

def difference(n1, n2):
    return n1 - n2

def product(n1, n2):
    return n1 * n2

def quotient(n1, n2):
    return n1 / n2

start = prompt_input()

n1 = float(start[0])
n2 = float(start[1])

plus = sums(n1, n2)
minus = difference(n1, n2)
prod = product(n1, n2)
quot = quotient(n1, n2)

print(f'What is the first number? {n1} \nWhat is the second number? {n2}\n{n1} + {n2} = {plus}\n\
{n1} - {n2} = {minus}\n{n1} * {n2} = {prod}\n{n1} / {n2} = {quot}')
