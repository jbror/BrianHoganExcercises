def mad_lib():

    prompt_noun = input('Hey! Give me a Noun:  ')
    prompt_verb = input('I need a Verb from you, enter Verb: ')
    prompt_adjective = input('Also give me an Adjective: ')
    prompt_adverb = input('Enter an Adverb or die : ')

    output_story = f'Imagine a {prompt_adjective} {prompt_noun} that {prompt_verb} quietly on a windowsill, dreaming of becoming a famous {prompt_noun}. That\'s pretty neat yo!'
    print(output_story)
start = mad_lib()



