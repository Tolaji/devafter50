print('\n~~~~~~~~~~~ Meal Price Calculator ~~~~~~~~~~~~~\n')

#Meals, children, adults and tax input block
childs_meal = float(input(f"What is the price of a child's meal? "))
adults_meal = float(input(f'What is the price of an adults meal? '))
num_of_children = int(input(f'How many children are there? '))
num_of_adults = int(input(f'How many adults are there? '))
sales_tax = float(input(f'what is the sales tax? '))
print()

#Calculations block
children_subtotal = childs_meal * num_of_children
adults_subtotal = adults_meal * num_of_adults
subtotal = (children_subtotal + adults_subtotal)
tax = subtotal * (sales_tax / 100)
total = subtotal + sales_tax
print()

#Calculations Summary block
print(f'Subtotal:', subtotal)
print(f'Sales Tax:', tax)
print(f'Total:', total)
print()

#Actual payments block
payment_amount = float(input('What is the payment amount? '))
change = payment_amount - total
print('change: ',change)
print()