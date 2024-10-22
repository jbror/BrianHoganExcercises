def prompt_input():
    while True:
        try:
            first_num = float(input('Hi! Give me number '))
            second_num = float(input('I need a number again, pls! '))
            return first_num, second_num
        except ValueError:
            print('Only numbers!')
def plus(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divided(n1, n2):
    return n1 / n2

start = prompt_input()

n1 = float(start[0])
n2 = float(start[1])

sums = plus(n1, n2)
difference = minus(n1, n2)
product = multiply(n1, n2)
quotient = divided(n1, n2)

print(f'What is the first number? {n1} \nWhat is the second number? {n2}\n{n1} + {n2} = {sums}\n\
{n1} - {n2} = {difference}\n{n1} * {n2} = {product}\n{n1} / {n2} = {quotient}')
