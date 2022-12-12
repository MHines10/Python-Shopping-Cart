# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.


def shop_cart():
    #empty lists for items and price of item
    shopcart_items = []
    shopcart_price = []
    
    # User Message
    print("Your Shopping Cart\n")
    
    # Loops until the user finishes shopping 
    while True:
        # Ask user to choose an action
        shop_opt = input("Would you like to Add, Remove or View your cart? If your finished shopping, type Done...\n ")
        
        # add item to the shopping cart
        if shop_opt.lower() == 'add':
            cart_item = input("\nWhat item would you like to add your cart?\n")
            item_price = input(f"What's the price for {cart_item.title()}?\n")
            shopcart_items.append(cart_item)
            shopcart_price.append(int(item_price))
            print(f"{cart_item.title()} for ${item_price} has been added to your cart.\n")
            
        # remove an item from the shopping cart
        elif shop_opt.lower() == 'remove':
            remove_item = input("What would you like to remove from your cart?\n")
            remove_price = input(f"What was the price of the {remove_item.title()}?\n")
            shopcart_items.remove(remove_item)
            shopcart_price.remove(int(remove_price))
            print(f"{remove_item.title()} has been removed from your cart.\n")
            
        # view the shopping cart
        elif shop_opt.lower() == 'view':
            print("Your Shopping Cart contains:")
            for item in shopcart_items:
                print(item)
            print(f"Current total: ${sum(shopcart_price)}")
        
        # quits the program
        elif shop_opt.lower() == 'done':
            break
    # user receipt
    for price in shopcart_price:
        print(f"Your receipt:")
        print(", ".join(str(i.title()) for i in shopcart_items))
        print(f"Your Total:\n ${sum(shopcart_price)}: Quantity of {len(shopcart_items)} items.")
        
shop_cart()