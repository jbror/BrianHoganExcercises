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
            binput =float(input('Enter bill amout, only numbers\n'))
            if type(binput) == float:
                break
        except ValueError:
            print('Only numbers!')

    while True: #Kollar så tip amount (procent) blir rätt input
        try:
            tinput =int(input('Enter the tip percentage, only numbers\n'))
            if type(tinput) == int:
                break
        except ValueError:
            print('Only numbers!')

    return binput, tinput



ci = check_input()
#print(ci)






