#Retirement Calculator
import datetime

def prompt_ages():
    try:
        prompt_age = float(input('What\'s your age?'))
        prompt_retirement_age = float(input('At what age would you like to retire in?'))
        return prompt_age, prompt_retirement_age
    except ValueError:
        print('Only floats!')


def count_years(current_age, age_retirement):
    return age_retirement - current_age
    #print(age_retirement - current_age)





start = prompt_ages()

age = start[0]
retirement_age = start[1]



check_years = count_years(age, retirement_age)























"""
current_time = datetime.datetime.now()

print(current_time.year)
print(current_time)

"""
