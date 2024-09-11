def ask_for_name ():
    get_name = input ('Hi there! Please tell me your name\n')
    return get_name.lower()

def greet(name):
    if name == 'glenn':
        print('Hallå änna Glenn')
    elif name == 'erik':
        print('Tjena Brush')
    elif name == 'alfred':
        print('Tjena Brush')
    else:
        print(f"Hello {name.capitalize()}, it's nice to meet you. Bengt is the one true god. Go in peace!")
get_name = ask_for_name()
greet(get_name)
