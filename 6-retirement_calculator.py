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
    current_time = datetime.datetime.now()

    return age_retirement - current_age + current_time.year, age_retirement - current_age


start = prompt_ages()
age = start[0]
retirement_age = start[1]
check_years = count_years(age, retirement_age)
current_time = datetime.datetime.now()

print(f'Hello! I will soon inform you how long it is left until total freedom.\nPLEASE be seated... \n')
time.sleep(3)

print(f'You are now {age:.0f} years old. You want to retire when you are {retirement_age:.0f} years old. \
The year is now {current_time.year} and the year when total freedom starts(aka retirement) for you is {check_years[0]:.0f}. \
That is only {check_years[1]:.0f} years away!! Prepare and enjoy =)')

