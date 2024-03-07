import random

print("Welcome to Mastermind!")
print("Choose a game mode:")
mode = int(input("1) Auto\n"
                 "2) Manual\n "))
if mode == 1:
    code = random.randint(10000, 99999)
    print(f"Code contains {len(str(code))} digits")
    qtyPos, qtyRight = 0, 0
    while qtyPos != len(str(code)):
        qtyPos, qtyRight = 0, 0
        guess = input("Your guess: ")
        for i in range(len(guess)):
            if guess[i] in str(code):
                qtyRight += 1
        code_str = str(code)
        for i in range(len(guess)):
            if guess[i] == code_str[i]:
                qtyPos += 1
        print(f"\nNumbers guessed right = {qtyRight}\nNumbers on the correct position = {qtyPos}\n")
    print("You are a winner!")
elif mode == 2:
    code = input("Secret code: ")
    print("\n" * 100)
    print(f"Code contains {len(code)} digits")
    qtyPos, qtyRight = 0, 0
    while qtyPos != len(str(code)):
        qtyPos, qtyRight = 0, 0
        guess = input("Your guess: ")
        for i in range(len(guess)):
            if guess[i] in str(code):
                qtyRight += 1
        code_str = str(code)
        for i in range(len(guess)):
            if guess[i] == code_str[i]:
                qtyPos += 1
        print(f"\nNumbers guessed right =  {qtyRight} \nNumbers on the correct position = {qtyPos}\n")
    print("You are a winner!")