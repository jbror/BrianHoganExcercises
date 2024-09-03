#The solution should follow these constraints:
#Enter the tip as a percentage. For example, a 15% tip
#would be entered as 15, not 0.15. Your program should
#handle the division.
#Round fractions of a cent up to the next cent.
#Ensure that the user can enter only numbers for the bill
#amount and the tip rate. If the user enters non-numeric values, display an appropriate message and exit the
#program.
#Instead of displaying an error message and exiting the
#program, keep asking the user for correct input until it
#is provided.
#Don’t allow the user to enter a negative number.
#Break the program into functions that do the computa-
#tions.

def check_input():
    while True: #Kollar så bill amount blir rätt input
        try:
            binput =float(input('Enter bill amout, only numbers(non negative!)\n'))
            if type(binput) == float and binput >= 0:
                break
        except ValueError:
            print('Only numbers!')

    while True: #Kollar så tip amount (procent) blir rätt input
        try:
            tinput =int(input('Enter the tip percentage, only numbers(non negative!\n'))
            if type(tinput) == int and tinput >= 0:
                break
        except ValueError:
            print('Only numbers!')

    return binput, tinput



ci = check_input() #Här tar vi inputen och kollar så den anges rätt.

bill_amount = ci[0] #Sparar notan
tip_rate = ci[1] #Sparar procentvärdet av tip som vi vill betala


def calculate_given_input(bill_input, tip_input):

    tip_amount = bill_input * (tip_input / 100)
    total = bill_input + tip_amount

    return total, tip_amount #Ger oss totalen att betala samt hur mycket som är tips



calculations = calculate_given_input(bill_amount, tip_rate)


tip_given = calculations[1]
final_amount = calculations[0]





def display_output(bill_without_tip, tip_percentage_given, output_tip, output_final_amount): # Här skickar vi med allt som ska visas. Notan utan tips, hur mycket tips vi vill ge, tips vi betalar, och slutsumman för notan med tips.



    print(f"The bill with non tip is {bill_without_tip:.2f}!")
    print(f"The percentage tip is set to {tip_percentage_given}%")
    print()
    print(f'Total bill is {output_final_amount:.2f}')
    print(f'The tip you pay is {output_tip:.2f}')





display = display_output(bill_amount, tip_rate, tip_given, final_amount)


