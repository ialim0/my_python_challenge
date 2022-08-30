#Step 4

import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

m = []
a = 6
num = 0
b = []
display = ""
for i in range(len(chosen_word)):
    m.append('_')
    display += m[i]

while a > 0 and display != chosen_word:
    guess = input("Guess a letter: \n").lower()
    for i in range(len(display)):

        if guess == chosen_word[i]:

            num += 1

            display = display[:i] + guess + display[i + 1:]

    if num <= 0:
        print(stages[a])
        a = a - 1
    num = 0

    print("Your guess:\n", display)

if display != chosen_word:
    print(stages[a])
    print('You lost')
else:
    print('You win')
