class SupermarketItem: # This will represent an item

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Checkout:
    MOMS = 0.25 # Tax rate (Moms in Swedish!)

    def __init__(self):
        self.items = [] # Store all SupermarketItem objs here

    def add_item(self, price, quantity):
        self.items.append(SupermarketItem(price, quantity))


    def calculate_tax(self,item, all_item = 1 ): # This calculates tax on the given item!
        if all_item == 0:
            return item.price * self.MOMS
        else:
            return item.total_price() * self.MOMS

    #def total_price_with_tax # HERE!!! --- tax + total_price yo!!

    def print_receipt(self): # prints out the receipt and displays all the items with quantity and price. Also shows total price with moms(tax!) in SEK.
        print('Receipt\n')
        for i, item in enumerate(self.items, start=1):
            tax_per_item = self.calculate_tax(item, all_item = 0)
            total_tax_for_item = self.calculate_tax(item)

            print(f'Item {i}: {item.quantity:.0f} pcs and each cost {item.price:.2f}:- SEK. Total without MOMS: {item.total_price()}:- SEK. ')
            print(f' MOMS per item is {tax_per_item}:- SEK. Total price with MOMS {total_tax_for_item}:- SEK')





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
    #checkout.calculate_tax()




if __name__ == "__main__": # Kör inte min funktion "main" om jag importerar scriptet. Alltså körs bara koden om jag kör den direkt. Testar..
    main()












