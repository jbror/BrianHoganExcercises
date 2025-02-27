class SupermarketItem:
    def __init__(self, price, quantity, tax_rate=0.25):
        self.price = price
        self.quantity = quantity
        self.tax_rate = tax_rate  # Change the taxrate here! In Sweden, MOMS = 25%

    def total_price(self):
        return self.price * self.quantity

    def tax_per_item(self):
        return self.price * self.tax_rate

    def total_tax(self):
        return self.total_price() * self.tax_rate

    def total_price_with_tax(self):
        return self.total_price() + self.total_tax()


class Checkout:
    def __init__(self):
        self.items = [] # Store all SupermarketItem objs here

    def add_item(self, price, quantity):
        self.items.append(SupermarketItem(price, quantity))

    def final_total_price(self):
        return sum(item.total_price_with_tax() for item in self.items)

    def final_total_price_without_tax(self):
        return sum(item.total_price() for item in self.items)

    def print_receipt(self):
        print('\n' + 'RECEIPT'.center(30, '.'))
        # prints my output!
        for i, item in enumerate(self.items, start=1):
            print(f'Item {i}: {item.quantity} pcs @ {item.price:.2f} SEK each')
            print(f'  - Total before tax: {item.total_price():.2f} SEK') # Price for item without tax
            print(f'  - Tax per item: {item.tax_per_item():.2f} SEK') # Tax for each "unit" of item
            print(f'  - Total tax: {item.total_tax():.2f} SEK') # Total tax per item (all units)
            print(f'  - Final price: {item.total_price_with_tax():.2f} SEK\n') # Final price of item

        final_price_without_tax = self.final_total_price_without_tax()
        final_price = self.final_total_price()
        print(f'Total amount without tax: {final_price_without_tax:.2f} SEK') # Final price with tax (bill amount)
        print(f'Total amount with tax: {final_price:.2f} SEK') # Final price with tax (bill amount)


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
        if quantity is None:
            break # If user enter 'done' here...

        checkout.add_item(price, quantity)

    checkout.print_receipt() # Outside the loop so no more items. Lets print the receipt


if __name__ == "__main__": # Kör inte min funktion "main" om jag importerar scriptet. Alltså körs bara koden om jag kör den direkt. Testar..
    main()


