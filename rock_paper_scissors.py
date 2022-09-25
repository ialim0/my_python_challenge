import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
tab=[rock,paper,scissors]
try:
    your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice=random.randint(0,2)


    if (your_choice==0 and computer_choice==2) or (your_choice==2 and computer_choice==1) or (your_choice==1 and computer_choice==0):
        print(f"You choose:\n{tab[your_choice]}")
        print(f'Computer choose:\n{tab[computer_choice]}')
        print("You win")
    elif your_choice==computer_choice :
        print(f"You choose:\n{tab[your_choice]}")
        print(f'Computer choose:\n{tab[computer_choice]}')
        print("You have to replay")

    else :
        print(f"You choose:\n{tab[your_choice]}")
        print(f'Computer choose:\n{tab[computer_choice]}')
        print("You lose.")
except ValueError:
    print(f"You choose:\n{tab[your_choice]}")
    print(f'Computer choose:\n{tab[computer_choice]}')
    print('You lose')
    from random import randrange
    print(randrange(10))

    
    

    



    
    
    