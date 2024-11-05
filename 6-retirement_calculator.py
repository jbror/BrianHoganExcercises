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


def calculate_retirement_year(current_age, chosen_year_for_retirement):
    current_time = datetime.datetime.now()
    calculate_retirement_year = chosen_year_for_retirement - current_age + current_time.year
    calculate_years_to_freedom = chosen_year_for_retirement - current_age
    return calculate_retirement_year, calculate_years_to_freedom


start_prompt = prompt_ages()
current_age = start_prompt[0]
chosen_year_for_retirement = start_prompt[1]
years_to_retirement = calculate_retirement_year(current_age, chosen_year_for_retirement)#Denna retunerar två värden/strängar. Året du pensionerar dig (total_freedom_year) och hur många år det är kvar till det året.
total_freedom_year = years_to_retirement[0]
current_time = datetime.datetime.now()

print(f'Hello! I will soon inform you how long it is left until total freedom.\nPLEASE be seated... \n')
time.sleep(3)
print(f'You are now {current_age:.0f} years old. You want to retire when you are {chosen_year_for_retirement:.0f} years old. \
The year is now {current_time.year} and the year when total freedom starts(aka retirement) for you is {total_freedom_year:.0f}. \
That is only {years_to_retirement[1]:.0f} years away!! Prepare and enjoy =)')
