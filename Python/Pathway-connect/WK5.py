"""
friends = []
friend = ""
while friend != "end":
    friend = input("Type the name of a friend: ")
    if friend != "end":
        friends.append(friend)
        print(f"Your friends are: {friend}")


for friend in friends:
    print(friend)

names = []
numbers = []


shopping_list = []
item = None
while item != "quit":
    item = input("Enter an item in the shopping list: ")
    if item != "quit":
        shopping_list.append(item)
print("The shopping list is: ")

for item in shopping_list:
    print("The shopping list with index is: ")
for index in range(len(shopping_list)):
    print([index], shopping_list[index])


# Display the shopping list with indexes using range
print("\nThe other shopping list with indexes is:")
for index in range(len(shopping_list)):
    print(f"{index}. {shopping_list[index]}")

    change_index = int(input("Whats the index of the item you want to change? "))
    new_item = input("State the name of the new item: ")

    shopping_list[change_index] = new_item
    print("The shopping list with indexes is:", shopping_list)

    for index in range(len(shopping_list)):
        print(index, shopping_list[index])
"""


# Create an empty list to store the shopping list
shopping_list = []

# Prompt the user to enter items for the shopping list
print("Please enter the items of the shopping list (type 'quit' to finish):")

# Loop to collect items from the user
while True:
    item = input("Item: ")
    if item.lower() == "quit":
        break
    shopping_list.append(item)

# Display the shopping list
print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

# Display the shopping list with indexes
print("\nThe shopping list with indexes is:")
for index, item in enumerate(shopping_list):
    print(f"{index}. {item}")

# Ask the user to choose an index to change
change_index = int(input("\nWhich item would you like to change? Enter the index: "))

# Ask the user for the new item
new_item = input("What is the new item? ")

# Update the shopping list with the new item
shopping_list[change_index] = new_item

# Display the updated shopping list with indexes
print("\nThe shopping list with indexes is:")
for index, item in enumerate(shopping_list):
    print(f"{index}. {item}")
