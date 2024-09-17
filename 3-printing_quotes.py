
def get_quotes():
    get_quotes = input('Enter any inspirational quotes about life, please!\n')
    get_author = input('Tell me the author or the mastermind behind that, i need to know!\n')

    return get_quotes, get_author

start = get_quotes()
print('A wise dude told me something great \"' + start[0] + '\" ' +'And that dude is the almighty ' + start[1].capitalize() +'.')
