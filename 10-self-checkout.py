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


    def calculate_item_tax(self,item, all_item = 1 ): # This calculates tax on given item (totalprice x tax) and also calculate tax on single item (price x tax) if argument 0 is given.
        if all_item == 0:
            tax_single_item = item.price * self.MOMS
            return tax_single_item

        else:
            total_tax_item = item.total_price() * self.MOMS
            return total_tax_item

    def final_item_price(self, item):
        final_price_item = item.total_price() * self.MOMS + item.total_price()
        return final_price_item

    def final_total_price(self): # THIS will get ME THE FINAL BILL PRICE! -- ´HERE WORK
        return


    def print_receipt(self): # prints out the receipt and displays all the items with quantity and price. Also shows total price with moms(tax!) in SEK.
        print('\n'+'RECEIPT'.center(21, '.'))
        for i, item in enumerate(self.items, start=1):
            tax_per_item = self.calculate_item_tax(item, all_item = 0)
            total_tax_for_item = self.calculate_item_tax(item)
            total_item_price_with_tax = self.final_item_price(item)
            #final_price_receipt = self.final_price_with_tax(item)


            print(f'Item {i}: {item.quantity:.0f} pcs and each cost {item.price:.2f}:- SEK. Total without MOMS: {item.total_price():.2f}:- SEK. ')
            print(f' MOMS per item is {tax_per_item:.2f}:- SEK. Total MOMS: {total_tax_for_item:.2f}:- SEK')
            print(f' Total price with MOMS is {total_item_price_with_tax:.2f}:- SEK.\n')
        #print(f'Total amount with MOMS: {final_price_receipt:.2f}:- SEK.')




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








