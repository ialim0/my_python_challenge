#This black_jack app can better with computer function and player function  
import random

tab = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     


def add(tab):
    som = 0
    for n in range(len(tab)):
        som = som + tab[n]
    return som


def computer():
    comp = []
    alp = random.sample(tab, k=2)
    for id in alp:
        if id != tab[0]:
            comp.append(int(id))
        else:
            if add(comp) <= 10:
                comp.append(int(11))
            else:
                comp.append(int(1))
    return comp


r = computer()

print(logo, )
continu = 'y'
t = []

continu = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':")
if continu == 'y':
    result = random.sample(tab, k=2)
    for elem in result:
        if elem == tab[0]:
            choix = int(input('What do you want to choose: 1 or 11: '))

            t.append(choix)

        else:
            t.append(int(elem))

    print('You', t, 'Computer:', r,
          f"your score is {add(t)} , computer score is :{add(r)}")
    pas = 'n'
    while pas == 'n':
        pas = input('Do you want to pass : y or n? ')
        if pas == 'n' and (add(t) < 21 or add(r) < 21):
            if random.choice(tab) == tab[0]:
                choix = int(input('What do you want to choose: 1 or 11: '))
                t.append(choix)

            else:
                t.append(random.choice(tab))
        if add(r) < 17 and pas == 'n':
            if random.choice(tab) == tab[0] and add(r) < 11:
                r.append(11)
            if random.choice(tab) == tab[0] and add(r) > 1:
                r.append(1)
        else:
            if add(r) < 18:
                r.append(random.choice(tab))

        if add(t) > 21:
            pas = 'y'
            print('You lose')
        elif add(r) > 21:
            pas = 'y'
            print('you win')
        elif pas == 'y' and add(r) > add(t):
            print('You lose')
        elif pas == 'y' and add(r) < add(t):
            print('you win')
        elif pas == 'y' and add(r) == add(t):
            print('Draw')

        print('You:', t, 'Computer:', r,
              f'Your score is {add(t)} and computer score is {add(r)} ')
