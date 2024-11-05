# Project builder
#
# Create a project that gives you a possibility to choose how hard do you want this project to be:
# 1. Easy: use only 2 things from the list like - list, if statements etc
# 2. Medium: use 4 things from the list like - list, if statements etc
# 3. Hard: use 6 things from the list like - list, if statements etc
#
# Here you will need to use:
# 1. Input
# 2. If statements
# 3. Random
# 4. List
import random

user_input = ''
bits_and_peaces = ['if', 'input', 'random', 'list', 'library', 'for', 'def', 'import', 'methods']
reward = ['buy yourself a treat', 'buy your friend a treat', 'buy yourself a piece of clothes', 'bake something', 'buy a flower to Maria']

while user_input != 'Easy' and user_input != 'Medium' and user_input !=  'Hard':
    user_input = input('''Hello, how hard do you want your project to be? Type one of the following choices:
1. Easy
2. Medium
3. Hard
''')

    if user_input == 'Easy':
       print('In your project please use the following python structures: ' + str(random.sample(bits_and_peaces, 2)))
       break

    elif user_input == 'Medium':
       print('In your project please use the following python structures: ' + str(random.sample(bits_and_peaces, 4)))
       break

    elif user_input == 'Hard':
       print('In your project please use the following python structures: ' + str(random.sample(bits_and_peaces, 6)))
       break

    else:
       print('You have entered something wrong, try again.')


print('After completing the task reward yourself with: ' + str(random.sample(reward, 1)))