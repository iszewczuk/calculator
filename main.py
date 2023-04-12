import math as mt

def starter():
    hello()
    wicd()
    entry()

def entry():
    while True: 
        operation = input("Select an operation to perform or type EXIT:")

        if operation.lower() == "exit":
            goodbye()
            break
        elif verify(operation) == False:
            print("Forbidden input")
        else:
            calculator(operation)

def verify(s):
    if s.isdigit():
        if int(s) > 6:
            print ("You can't choose count > 6")
            return False
        if int(s) == 0:
            print ("You can't choose zero")
            return False
    elif s.lstrip('-').isdigit():
        print ("You can't choose count < 0")
        return False
    elif not s.isdigit() and s.lower != 'exit':
        print("Please, try once again")
        return False
    return True

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Division by zero not allowed")
    else:
        return x / y

def pow(x, y):
    return x ** y

def sqrt(x, y):
    return x ** (1 / y)

def calculator(s):
    x = float(input("Enter first number:"))
    y = float(input("Enter second number:"))

    if s == "1":
        print(add(x, y))
    elif s == "2":
        print(substract(x, y))
    elif s == "3":
        print(multiply(x, y))
    elif s == "4":
        print(divide(x, y))
    elif s == "5":
        print(pow(x, y))
    elif s == '6':
        print(sqrt(x, y))

def hello():
    print(".---.  .---.     .-''-.    .---.     .---.       ,-----.             _______     ___    _  ______      ______        ____     __  ")
    print("|   |  |_ _|   .'_ _   \   | ,_|     | ,_|     .'  .-,  '.          \  ____  \ .'   |  | ||    _ `''. |    _ `''.    \   \   /  / ")
    print("|   |  ( ' )  / ( ` )   ',-./  )   ,-./  )    / ,-.|  \ _ \         | |    \ | |   .'  | || _ | ) _  \| _ | ) _  \    \  _. /  '  ")
    print("|   '-(_{;}_). (_ o _)  |\  '_ '`) \  '_ '`) ;  \  '_ /  | :        | |____/ / .'  '_  | ||( ''_'  ) ||( ''_'  ) |     _( )_ .'  ")
    print("|      (_,_) |  (_,_)___| > (_)  )  > (_)  ) |  _`,/ \ _/  |        |   _ _ '. '   ( \.-.|| . (_) `. || . (_) `. | ___(_ o _)'    ") 
    print("| _ _--.   | '  \   .---.(  .  .-' (  .  .-' : (  '\_/ \   ;        |  ( ' )  \' (`. _` /||(_    ._) '|(_    ._) '|   |(_,_)'     ")
    print("|( ' ) |   |  \  `-'    / `-'`-'|___`-'`-'|___\ `\"/  \  ) /         | (_{;}_) || (_ (_) _)|  (_.\.' / |  (_.\.' / |   `-'  /      ")
    print("(_{;}_)|   |   \       /   |        \|        \'. \_/``\".'           |  (_,_)  / \ /  . \ /|       .'  |       .'   \      /       ")
    print("'(_,_) '---'    `'-..-'    `--------``--------`  '-----'            /_______.'   ``-'`-'' '-----'`    '-----'`      `-..-'        ")


def wicd():
    print(" _____ _     _                   _   _           _     _                         _        ")
    print("/__   \ |__ (_)_ __   __ _ ___  | |_| |__   __ _| |_  (_)   ___ __ _ _ __     __| | ___ _ ")
    print("  / /\/ '_ \| | '_ \ / _` / __| | __| '_ \ / _` | __| | |  / __/ _` | '_ \   / _` |/ _ (_)")
    print(" / /  | | | | | | | | (_| \__ \ | |_| | | | (_| | |_  | | | (_| (_| | | | | | (_| | (_) | ")
    print(" \/   |_| |_|_|_| |_|\__, |___/  \__|_| |_|\__,_|\__| |_|  \___\__,_|_| |_|  \__,_|\___(_)")
    print("                     |___/                                                                ")
    print("1. ADD \n2. SUBSTRACT \n3. MULTIPLY \n4. DIVIDE\n5. POWER\n6. ROOT")


def goodbye():
    print("  _______   ______     ______    _______  .______   ____    ____  _______  __  ")
    print(" /  _____| /  __  \   /  __  \  |       \ |   _  \  \   \  /   / |   ____||  | ")
    print("|  |  __  |  |  |  | |  |  |  | |  .--.  ||  |_)  |  \   \/   /  |  |__   |  | ")
    print("|  | |_ | |  |  |  | |  |  |  | |  |  |  ||   _  <    \_    _/   |   __|  |  | ")
    print("|  |__| | |  `--'  | |  `--'  | |  '--'  ||  |_)  |     |  |     |  |____ |__| ")
    print(" \______|  \______/   \______/  |_______/ |______/      |__|     |_______|(__) \n")


starter()
