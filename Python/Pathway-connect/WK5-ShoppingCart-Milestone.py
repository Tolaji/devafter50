print("\n~~~ SHOPPING CART ~~~")
print("~~~ Milestone ~~~\n")

# Welcome
print("\nWelcome to the shopping cart programme\n")
print("*" * 50)


# Empty cart list
cart = []

# Loop
while True:
    # for item in cart:

    print("\nPlease select one of the following:")
    print("-" * 35)
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    # Prompt to store  user  actions
    action = int(input("Please enter an action: "))
    print("-" * 50)
    print()

    if action == 1:
        # Add items to cart
        item = input("what item would you want to add? ")
        cart.append(item)

        print("'" + item + "' has been added to the cart.\n")
        print("-" * 50)
        print()
        continue

    elif action == 2:
        print("The content of the shopping cart are:")
        # Display list of items in cart
        for item in cart:
            print(item)

    # elif action == 3:

    # elif action == 4:

    elif action == 5:
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid input, please try again")
