#Koden som är kommenterad är första uppgiften och koden utanför är den andra uppgiften eller extrauppgiften "Challange.

"""
def get_quotes():
    get_quotes = input('Enter any inspirational quotes about life, please!\n')
    get_author = input('Tell me the author or the mastermind behind that, i need to know!\n')

    return get_quotes, get_author

start = get_quotes()
print('A wise dude told me something great \"' + start[0] + '\" ' +'And that dude is the almighty ' + start[1].capitalize() +'.')
"""

#Uppgiften under "Challange" från boken.

quotes_authors = [
{'author': 'Hasse i Trelleborg', 'quote': '\"Den som lever livet är inte död.\"'},
{'author': 'DukeNuken', 'quote': '\"Eat shit or Die.\"'},
{'author': 'Bror Johansson', 'quote': '\"Ät massa glass så att du springer snabbt.\"'}
]

get_len = len(quotes_authors)
for i in range(get_len):
    print('A wise dude told me something great ' + quotes_authors[i]['quote'] + ' ' +'And that dude is the almighty ' + quotes_authors[i]['author'].capitalize() +'.')

print('\n' + 'And here it comes again in a similar way' + '\n')

for quotes_dict in quotes_authors:
    print('author ' + quotes_dict['author'])
    print('quote ' + quotes_dict['quote'])
