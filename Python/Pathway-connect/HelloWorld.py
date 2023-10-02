# Initialize name and favorite color to None
name = None
favorite_color = None

# Loop until both name and favorite color are captured
while not (name and favorite_color):
    # Prompt the user to enter a sentence containing their name and favorite color
    sentence = input('Hi, please introduce yourself and mention your name and favorite color: ')

    # Use string manipulation to extract name and favorite color
    words = sentence.split()  # Split the sentence into words
    for word in words:
        # Look for a word that matches common colors as the favorite color
        if word.lower() in ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'black', 'magenta', 'brown'] and not favorite_color:
            favorite_color = word
        # Look for a word that could be a name (starts with a capital letter)
        elif word[0].isupper() and not name:
            name = word

    # If name and favorite color are not captured, prompt the user again
    if not (name and favorite_color):
        print('I could not determine your name or favorite color in your introduction. Please try again.')
        print()

# Display the extracted name and favorite color
print()
print(f"Great! now i know Your name is '{name}' and your favorite color is '{favorite_color}'.")
print(f"Wow! '{favorite_color}' is a fantastic color, {name}!")
print()

#Hint
print('Now lets do some MatLib')
print()

#Example prompt insight
print('Please consider the following prompts before proceeding')
print()
print('adjective: ')
print('animal: ')
print('verb: ')
print('exclamation: ')
print('verb: ')
print('verb: ')
print()

# Prompt the user for inputs
adjective = input('Enter an adjective: ')
animal = input('Enter an animal: ')
verb1 = input('Enter a verb: ')
exclamation = input('Enter an exclamation: ')
verb2 = input('Enter another verb: ')
verb3 = input('Enter a third verb: ')

# Display the mad lib story with creativity and formatting
print('\n~~~ MAD LIB STORY ~~~\n')
print('The other day, I found myself in a " + adjective + " situation.')
print('As I was walking down the hallway, I suddenly encountered a ' + animal)
print('that was ' + verb1 + ' right towards me!')
print(f'"' + exclamation + '!"' + " I shouted, startled by the sight.")
print('But all I could do was to ' + verb2 +
      ' repeatedly, hoping to scare it away.')
print('Miraculously, my plan worked and the ' +
      animal + ' stopped in its tracks.')
print('However, it then tried to ' + verb3 + ' right in front of my family!')
print('It was quite a sight, and we all burst into laughter.')
print('In the end, it turned out to be a hilarious adventure!')
print('\n~~~~~~~~~~~~~~~~~~~~~\n')
