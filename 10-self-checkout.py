class SupermarketItem: # This will represent an item

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Checkout:
    # my pos
    def __init__(self):
        self.items = [] # Store my items here

def get_valid_number(prompt):

    # Make sure the input is valid
    while True:
        value = input(prompt)
        if value.lower() == 'done':
            return None
        try:
            number = float(value)
            if number < 0:
                print("Please enter a positive number.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")




def main():
    checkout = Checkout()
    print(1+1) # testar :P





if __name__ == "__main__": # Denna körs först
    main()














