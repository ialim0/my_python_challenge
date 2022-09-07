from random import randrange

logo = """ "    


                                                                                                                                           
                                                                                                                                           
  ,----..                                                                                              ____                                
 /   /   \                                                                                           ,'  , `.  ,---,                       
|   :     :          ,--,                                                ,---,          ,--,      ,-+-,.' _ |,---.'|               __  ,-. 
.   |  ;. /        ,'_ /|             .--.--.    .--.--.             ,-+-. /  |       ,'_ /|   ,-+-. ;   , |||   | :             ,' ,'/ /| 
.   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '           ,--.'|'   |  .--. |  | :  ,--.'|'   |  ||:   : :      ,---.  '  | |' | 
;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./          |   |  ,"' |,'_ /| :  . | |   |  ,', |  |,:     |,-.  /     \ |  |   ,' 
|   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_            |   | /  | ||  ' | |  . . |   | /  | |--' |   : '  | /    /  |'  :  /   
.   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `.         |   | |  | ||  | ' |  | | |   : |  | ,    |   |  / :.    ' / ||  | '    
'   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \        |   | |  |/ :  | : ;  ; | |   : |  |/     '   : |: |'   ;   /|;  : |    
'   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /        |   | |--'  '  :  `--'   \|   | |`-'      |   | '/ :'   |  / ||  , ;    
|   :    /  :  ,      .-./|   :    |'--'.     /'--'.     /         |   |/      :  ,      .-./|   ;/          |   :    ||   :    | ---'     
 \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'          '---'        `--`----'    '---'           /    \  /  \   \  /           
  `---`                     `----'                                                                           `-'----'    `----'            
                                                                                                                                           
                                                               
                                                                
    """

print(logo)


#A function to choose level
def flevel(level):

    if level == 'easy':
        return 10
    elif level == 'hard':
        return 5
    else:
        print('Choose the correct level to play')
        return 0


#Guess game function
def guess_game():
    print(
        "Welcome to the number guessing game\n:\n I'm thinking a number between 1 and 100 ."
    )
    level_choice = input('Choose a difficulty.Type easy or hard :')
    attempts = flevel(level_choice)
    guess_number = randrange(101)

    while attempts > 0:
        print('You have {} remaining to guess the number'.format(attempts))

        user_guess_number = int(input("Make a guess: "))
        if user_guess_number == guess_number:
            print("You got it.The answer is {}.".format(guess_number))
            attempts = 0
        elif user_guess_number < guess_number:
            print("Too low.")
            if attempts > 1:
                print("Guess again")

            attempts = attempts - 1
            if attempts == 0:
                print('You lose.')
        elif (user_guess_number > guess_number):
            print("Too high.")
            if attempts > 1:
                print("Guess again")

            attempts = attempts - 1
            if attempts == 0:
                print('You lose.')


guess_game()
