#create predefine catalogue using a dictionary for the product management
products = {
    "Egg": {"price": 1200, "stock": 29},
    "Bread": {"price": 500, "stock": 16},
    "Pepsi": {"price": 150, "stock": 63},
    "Orange": {"price": 1400, "stock": 30},
    "Soap": {"price": 650, "stock": 34},
    "Trashbag": {"price": 400, "stock":25},
    "Yogourt": {"price": 1200, "stock": 30},
    "Beef": {"price": 800, "stock": 25},
    "Coffee": {"price": 1000, "stock": 35},
    "Rice": {"price": 1500, "stock": 38}
}

#Display the available products
def display_products():
    print("\nAvailable Products:")
    print(f"{'Product':<10}{'Price':<10}{'Stock':<10}")
    l_stock = 5  # Set low stock threshold
    for product, details in products.items():
        print(f"{product:<10}{details['price']:<10}{details['stock']:<10}")
        if details['stock'] <= l_stock:
            print(f"  -> {product} is low on stock!")

class ShoppingCartOps: # defining a class
    def __init__(self):
        self.cart = {}  # Empty cart list

    def add_to_cart(self):
        product = input("Enter product name: ").strip() #Prompting to enter product name and using the .strip function so the program doesnt show an error if the string entered is not the same as the one in the list.
        if product not in products:    #if the product entered is not in the dictionary
            print("Product not found.")
            return

        while True: #Keep asking until valid input
            try: #Tesing code for  errors
                quantity = int(input("Enter quantity: ")) #Enter the quantity
                if quantity <= 0: # if the quantity is less than 0 then
                    print("Quantity must be greater than 0.") 
                    continue
                if quantity > products[product]["stock"]:
                    print("Not enough stock available.")
                    continue
                break
            except ValueError: #Handling invalid inputs
                print("Invalid input. Please enter a number")

            #Check if item already in cart
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity
        
        products[product]["stock"] -= quantity
        print(f"{quantity} {product}(s) added to cart.")

    #checks if product is in cart before removing and updates stock after removing
    def remove_from_cart(self):
        product = input("Enter product name to remove: ").strip()
        if product in self.cart:
            products[product]["stock"] += self.cart[product]
            del self.cart[product]
            print(f"{product} removed from cart.")
        else:
            print("Product not found in cart.")
    
    def show_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        total_cost = 0  #expected to store  the  cost of all items
        print("\nYour Shopping Cart:") #shopping cart header
        print(f"{'Product':<10}{'Quantity':<10}{'Total Price':<10}")
        print("-" * 30)
        for product, quantity in self.cart.items():
            price = products[product]["price"]
            cost = price * quantity
            total_cost += cost
            print(f"{product:<10}{quantity:<10}{cost:<10}")
        print("-" * 30)
        print(f"\nTotal Cost: {total_cost}")
    
    def checkout(self):
        if not self.cart:
            print("Your carts is empty.")
            return

        subtotal = sum(products[product]["price"] * quantity for product, quantity in self.cart.items())
        tax = subtotal * 0.10
        total_cost = subtotal + tax
        discount = total_cost * 0.05 if total_cost > 5000 else 0
        total_cost -= discount

        print("\n         RECEIPT ")
        print("STORE NAME: UC mart")
        print("")
        print(f"{'Product':<10}{'Qty':<6}{'Price':<10}{'Total':<10}")
        print("-" * 40)
        for product, quantity in self.cart.items():
            price = products[product]["price"]
            cost = price * quantity
            print(f"{product:<10}{quantity:<6}{price:<10}{cost:<10}")
        print("-" * 40) 
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax (10%): {tax:.2f}")
        print(f"Discount (5% for orders over $5000): {discount:.2f}")
        print(f"Total Amount Due: {total_cost:.2f}")
        print("-" * 40)

        while True:
            try:
                amount_paid = float(input("Enter payment amount: "))
                if amount_paid < total_cost:
                    print("Insufficient payment. Please enter the full amount.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric amount.")

        change = amount_paid - total_cost
        print(f"Amount Paid: {amount_paid:.2f}")
        print(f"Change Returned: {change:.2f}")
        print("_________________________")
        print("Thank You for Shopping with Us!")
        print("___________________\n")
        
        self.cart.clear()
        print("Checkout complete.")

        decision = input("Would you like to do another transaction? ").strip()
        if decision == 'Yes':
            cart.add_to_cart()
        
            
    

        


# POS System Menu
cart = ShoppingCartOps()
while True:
    print("\n       Point of Sale System ")
    print("1. Display Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        display_products()
    elif choice == "2":
        cart.add_to_cart()
    elif choice == "3":
        cart.remove_from_cart()
    elif choice == "4":
        cart.show_cart()
    elif choice == "5":
        cart.checkout()
    elif choice == "6":
        confirm  = input("Are you sure you want to exit? (yes/no): ").strip()
        if confirm == "yes":
            print("Exiting POS system. Goodbye!")
            break
        else:
            print("Returning to menu.")
    else:
        print("Invalid choice. Please enter a valid option.")