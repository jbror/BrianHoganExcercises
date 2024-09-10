
#The “Hello, World” program is the
#first program you learn to write in many languages, but it doesn’t involve any input.
#So create a program that prompts for your name and printsa greeting using your name.

#Example Output
#What is your name? Brian
#Hello, Brian, nice to meet you!

#Constraints
#Different people deserve different greetings.

#The default greeting is, as presented above, "Hello, [name], nice to meet you!"
#But there are certain exceptions:

#Here is a list names that should have certain greetings
#"Glenn" -> "Hallåå eller änna Glenn"
#"Alfred", "Erik" -> "Tjena brorsan"

#And as in the previous excercise, try to structure your program into meaningful functions and be mindful in how you name them.



def ask_for_name ():

    get_name = input ('Hi there! Please tell me your name\n')
    return get_name.lower()


def put_exceptions_here(): #Här bakar jag in listan med undantag i en funktion. Kallar man på funktionen får du listan som lower().

    exceptions = [
    'Alfred',
    'Glenn',
    'Erik',
    ]

    exceptions_lower = [x.lower() for x in exceptions] # Gör listan med namn som är "undantag" till lower
    return exceptions_lower


def greet(name):

    if name == 'glenn':
        print('Hallå änna Glenn')

    elif name == 'erik':
        print('Tjena Brush')

    elif name == 'alfred':
        print('Tjena Brush')

    else:
        print(f"Hello {name.capitalize()}, it's nice to meet you. Bengt is the one true god. Go in peace!")

exceptions = put_exceptions_here()
get_name = ask_for_name()
greet(get_name)

