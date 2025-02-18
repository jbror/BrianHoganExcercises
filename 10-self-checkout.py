class SupermarketItem: # This will represent an item

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Checkout:
    MOMS = 0.25 # Tax rate (Moms in swedish!)

    def __init__(self):
        self.items = [] # Store all SupermarketItem objs here

    def add_item(self, price, quantity):
        self.items.append(SupermarketItem(price, quantity))
        #print(len(self.items))

    def calculate_tax(self):
        if self.items:
            tax_per_item = self.items[-1]
            return tax_per_item.total_price() * self.MOMS
        return 0 # If no items, returns 0



    def print_receipt(self): # prints out the receipt and displays all the items with quantity and price. Also shows total price with moms(tax!) in SEK.
        print('Receipt\n')
        for i, item in enumerate(self.items, start=1):
            print(f'Item {i}: {item.quantity:.0f} and each cost {item.price:.2f}:- SEK. - {self.calculate_tax()} Total without MOMS is {item.total_price():.2f}:- SEK')


def get_valid_number(prompt):

    # checks for correct input
    while True: #TODO? Should the quantity only be ints? :o
        value = input(prompt)
        if value.lower() == 'done':
            return None
        try:
            number = float(value)
            if number < 0:
                print('Please enter a positive number.')
            else:
                return number
        except ValueError:
            print('Invalid input. Please enter a numeric value.')




def main():

    checkout = Checkout() # Creates my object

    while True:
        price = get_valid_number("Enter the price of the item (or 'done' to finish): ")
        if price is None:
            break  # Exit loop if user enters 'done'
        quantity = get_valid_number('Enter the quantity: ')
        if quantity is None:
            break # If user enter 'done' here...

        checkout.add_item(price, quantity)

    checkout.print_receipt() # Outside the loop so no more items. Lets print the receipt
    checkout.calculate_tax()




if __name__ == "__main__": # Kör inte min funktion "main" om jag importerar scriptet. Alltså körs bara koden om jag kör den direkt. Testar..
    main()












