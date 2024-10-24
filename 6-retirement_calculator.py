#Retirement Calculator
import datetime
import time

def prompt_ages():
    while True:
        try:
            prompt_age = float(input('What\'s your age? '))
            prompt_retirement_age = float(input('At what age would you like to retire in? '))
            return prompt_age, prompt_retirement_age
        except ValueError:
            print('Only floats!')


def count_years(current_age, age_retirement):
    return age_retirement - current_age



#display_years_until_freedom =




start = prompt_ages()

age = start[0]
retirement_age = start[1]

check_years = count_years(age, retirement_age)



print(f'Hello! I will soon inform you how long it is left until total freedom.\nPLEASE be seated... \n')
time.sleep(3)







"""
current_time = datetime.datetime.now()

print(current_time.year)
print(current_time)

"""
