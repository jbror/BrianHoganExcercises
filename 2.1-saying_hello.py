
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

def askforname ():

    get_name = input ('Hi there! Please tell me your name\n')
    return get_name.lower()




def check_exceptions (name, exceptions_lower):

    if name in exceptions:
        print('Is here')

    else:
        print('not here')

def put_exceptionshere(): #Här bakar jag in listan med undantag i en funktion. Kallar man på funktionen får du listan som lower().

    exceptions = [
    'Alfred',
    'Glenn',
    'Erik',
    ]

    exceptions_lower = [x.lower() for x in exceptions] # Gör listan med namn som är "undantag" till lower
    return exceptions_lower




exceptions = put_exceptionshere()
get_name = askforname()

check_exceptions(get_name, exceptions)
