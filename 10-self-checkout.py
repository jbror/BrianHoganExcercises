class SupermarketItem: # This will represent an item

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Checkout:
    # my pos
    def __init__(self):
        self.items = [] # Store all SupermarketItem objs here

    def add_item(self, price, quantity):
        self.items.append(SupermarketItem(price, quantity))
        #print(len(self.items))


    def print_receipt(self):
        print('Receipt\n')
        for i, stuff in enumerate(self.items, start=1):
            print(f'Item {i}: {stuff.quantity:.0f} and each cost {stuff.price:.2f}:- SEK Total without MOMS is {stuff.total_price():.2f}:- SEK')
            #print(f'kaka{(stuff.quantity)}')




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





if __name__ == "__main__": # Kör inte min funktion "main" om jag importerar scriptet. Alltså körs bara koden om jag kör den direkt. Testar..
    main()












