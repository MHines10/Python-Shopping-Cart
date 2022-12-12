# Initialize cart as empty list
cart = []

# Print welcome message
print("Welcome to the Shopping Cart Program!\n")

# Loop until user quits
while True:
    # Ask user to choose an action
    cart_item = input("Add item to your cart:\n").title()
    num_items = int(input("How many would you like?\n"))
    item_price = (input("Enter the price of the item:\n$"))
    action = input("What would you like to do? (add/delete/view/quit): ")
    
    # If action is add, add item to the shopping cart
    if action.lower() == 'add':
        item = input("What would you like to add? ")
        cart.append(item)
        
    # If action is delete, delete item from the shopping cart
    elif action.lower() == 'delete':
        item = input("What would you like to delete? ")
        cart.remove(item)
        
    # If action is view, print out the shopping cart
    elif action.lower() == 'view':
        print("Your cart contains:")
        for item in cart:
            print(item)
    
    # If action is quit, quit the program
    elif action.lower() == 'quit':
        break