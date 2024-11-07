#Retirement Calculator
import datetime
import time



def prompt_float(prompt):
    while True:
        try:
            data = float(input(prompt))
            return data
        except ValueError:
            print('Only floats!')


def calculate_retirement_year(current_age, chosen_year_for_retirement):
    current_time = datetime.datetime.now()
    retirement_year = chosen_year_for_retirement - current_age + current_time.year
    return retirement_year

def calculate_years_to_freedom(age, retirement_age):
    return retirement_age - age


current_time = datetime.datetime.now()
current_age = prompt_float('What\'s your age?')
retirement_age = prompt_float('At what age would you like to retire?')
retirement_year = calculate_retirement_year(current_age, retirement_age)
years_to_freedom = calculate_years_to_freedom(current_age, retirement_age)

print(f'Hello! I will soon inform you how long it is left until total freedom.\nPLEASE be seated... \n')
time.sleep(3)
print(f'You are now {current_age:.0f} years old. You want to retire when you are {retirement_age:.0f} years old. \
The year is now {current_time.year} and the year when total freedom starts(aka retirement) for you is {retirement_year:.0f}. \
That is only {years_to_freedom:.0f} years away!! Prepare and enjoy =)')

