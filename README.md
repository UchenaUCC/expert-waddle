# Best Buy Retail Store
***Authors: Uchena Miller; Chadwayne Smikle***
Date Created: April 5, 2025
Course: ITT103 | Programming Techniques
Github Public URL to Code: https://github.com/UchenaUCC/expert-waddle.git


# Point of Sale (POS) System - README

### Purpose of the Program:

This Python program simulates a point of sale (POS) system, allowing users to browse products, manage a cart, and perform checkout.

## Functionalities

1.  Display Products
    
    -   Shows a predefined catalogue of items with price and stock level.
    -   Alerts user if stock is low.
        
2.  Add to Cart
    
    -   Lets the user add products to their cart based on available stock.
    -   Automatically updates the stock quantity.
        
3.  Remove from Cart
    
    -   Removes an item from the user's shopping cart and restores it to inventory.
        
4.  View Cart
    
    -   Displays items in the cart along with total quantity and calculated cost.
        
5.  Checkout
    
    -   Computes subtotal, tax (10%), and discount (5% for purchases above $5000).
    -   Prompts for payment and calculates change.
    -   Generates a simple receipt.
    -   Clears the cart after successful checkout.
        
6.  Exit
    
    -   Allows user to safely exit the program with confirmation.

## Required (and optional) Modifications:

 - Add more products to the `products` dictionary as needed.
 
 - Improve validation so product names are case-insensitive or suggest similar products if input is incorrect.

 - Implement databases for proper inventory management.

 - Transaction History: Record each transaction with timestamp, items bought, and amount paid to a text or log file.

 - Allow users to search for products by name or category

## Assumptions and Limitations:

 - All product names must be typed exactly as shown when adding/removing from the cart.

 - The product catalogue is hardcoded and not stored in an external database or file.

 - Only one transaction is handled at a time

 - The POS runs in the terminal and does not have a graphical interface.
