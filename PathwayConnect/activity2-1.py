color = 'blue'
animal = 'horse'
print(color+animal)
print(color + '' + animal + '!')
combined_words = color + '' + animal + '!'
print(combined_words)

print()
boys_count = 10
girls_count = 11
print()
print(boys_count + girls_count)
total_count = boys_count + girls_count
print(total_count)
print()
apple_count = 5
'''
print('You have' + apple_count + 'apples')10
'''
length_num = 50
width_num = 10
print(length_num + width_num)
print()
length_string = str(length_num)
width_string = str(width_num)
print(length_string + width_string)
print()
quantity_from_user = input('How many items do you have? ')
quantity_number = int(quantity_from_user)
double_number = quantity_number * 2
print(double_number)
print()
cars = 346
people = 8
people_per_car = people / cars
print(f'There are {people_per_car:.1f} people in each car.')
print()
print(f'There are {people_per_car:.2f} people in each car.')
print()
print(f'There are {people_per_car:.3f} people in each car.')
print()
distance = 9 * 1205 * 18
print(f'The distance is: {distance:.3e} meters.')
print()
print(f'The distance is: {distance:.6e} meters.')
print()
big_number = 123456789
print(f'The number is: {big_number}')
print(f'The number is: {big_number:,}')
print(f'The number is: {big_number:_}')
print()

fahrenheit = float(input('What is the temperature in fahrenheit? '))
celsius = (fahrenheit - 32) * 5/9
print(f'The temperature in celsius is {celsius:.1f}')

print()

#Meals, children, adults and tax input block
childs_meal = float(input(f"What is the price of a child's meal? "))
adults_meal = float(input(f'What is the price of an adults meal? '))
num_of_children = int(input(f'How many children are there? '))
num_of_adults = int(input(f'How many adults are there? '))
sales_tax = float(input(f'what is the sales tax? '))
print()

#Variable assignments and calculations block
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
print('change: $', change)
print()