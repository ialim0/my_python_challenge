
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(n1, n2):
    """
    addition
    """
    return n1 + n2


def min(n1, n2):
    """
    minus
    """
    return n1 - n2


def multi(n1, n2):
    """
    multiplication
    """
    return n1 * n2


def divide(n1, n2):
    """
    divide
    """
    return n1 / n2


n1 = float(input("What is  the first number: "))
operation = {'+': add, '-': min, '*': multi, '/': divide}
end=False 
while end==False:
    sym = input('Pick an operation\n')
    n2 = float(input("What is the next number\n"))
    symb = operation[sym](n1, n2)

    print(f"{n1} {sym} {n2}={symb}")
    check=input("Do you want another calculation?: yes ,no:\t")
    if check=='no':
        end=True
    else:
        n1=symb
    

    
