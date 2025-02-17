class SupermarketItem: # This will represent an item

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        #all_items.append(price, quantity)

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
        for i, stuff in enumerate(self.items, start=0):
            print(f'yo {i} yo2 {stuff.price:.2f} yo3')
            print(f'kaka{(stuff.quantity)}')




def get_valid_number(prompt):

    # checks for correct input
    while True:
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

        checkout.add_item(price, quantity)

    checkout.print_receipt() # Outside the loop so no more items. Lets print the receipt





if __name__ == "__main__": # Kör inte min funktion "main" om jag importerar scriptet. Alltså körs bara koden om jag kör den direkt. Testar..
    main()












