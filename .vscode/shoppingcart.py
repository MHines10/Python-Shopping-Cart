# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

def shop_cart():
 
    cart = []
    while True:
            cart_item = input("Add item to your cart:\n").title()
            num_items = int(input("How many would you like?\n"))
            item_price = (input("Enter the price of the item:\n$"))
            cart[cart_item] = {'amount': num_items, 'price': item_price}
            print(f"Added to your cart: Item {cart_item} Amount {num_items}\n")
        
            
            shop_opt = input("""To Add or Remove an item or to View your cart:
        Type: Add, Remove or View\n
    If you are finished shopping:
        Type: Done\n""")
            if shop_opt.lower() == "add":
                continue
                cart_item.item(cart)
                
            elif shop_opt.lower() == 'view':
                print("Your cart contains:")
            for item in cart.keys():
                print(f"{num_items} {item}")
            
            
            if shop_opt == "done":
                break
        for cart_item,info in cart.items():
            print(cart_item + ": Amount: " + str(info['amount']) + ": Price: " + str(info['price']))
        
            
            # print("{cart_item}: Ammount:{info['ammount']} Price: ${info[]}:  total $")
        return cart
        

shop_cart()