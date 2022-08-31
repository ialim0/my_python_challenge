logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP""" """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""" """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
print(logo)


def app():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    result = 0
    x = text.split()
    if direction == "encode":
        b = ""
        c = ""
        for i in range(len(x)):
            b = b + x[i]
        for i in range(len(b)):

            k = alphabet.index(b[i]) + shift
            if k > 25:
                k = k % 26
            c = c + alphabet[k]
        result = c

    if direction == "decode":
        init_1 = ""
        init_2 = ""

        for i in range(len(x)):
            init_1 = init_1 + x[i]
        for i in range(len(init_1)):
            k_1 = alphabet.index(init_1[i]) - shift
            if k_1 < 0:
                k_1 = k_1 % 26
            init_2 = init_2 + alphabet[k_1]
        result = init_2
    print(result)


end_game = 'yes'
while end_game == 'yes':

    app()
    end_game = input("Do you want to continue? Yes or No\n").lower()
if end_game == 'no':
    print('Merci pour la confiance\n')
