import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''




def bet():
    dictionary={}
    name=''
    end=False
    while end==False:
        print(logo,"\n Welcome to the secret aution program.")
        name=input('What\'s your name: ')
        dictionary[name]=int(input("What's your bid: $"))
        check=input('Are there any other bider?:yes or no: ').lower()
        if check=='yes':
            end=False
            os.system('clear')

        else:
            end=True
    win = max(dictionary, key=dictionary.get)
    print(f'The winner of the bid is :  *** {win}  ***')


bet()
    
    




    
    
    