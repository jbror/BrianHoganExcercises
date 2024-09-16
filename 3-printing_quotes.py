


def print_quotes():
    get_quotes = input('Enter any inspirational quotes about life, please!\n')
    get_author = input('Tell me the author or the mastermind behind that, i need to know!\n')

    return get_quotes, get_author






start = print_quotes()

print(start[0] +' ' + start[1])
