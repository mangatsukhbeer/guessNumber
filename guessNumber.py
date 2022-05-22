import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if(guess < random_number):
            print(f"Sorry, Guess again, TOO LOW")
        elif(guess > random_number):
            print(f"Sorry, Guess again, TOO HIGH")

    print(f"You Did it!!!!! Number is {guess}")

def AI_Guess(x):
    high = x
    low = 1
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f"is {guess} too high [H] or too low [L] or correct [C]")
        if feedback == 'H' or feedback == 'h':
            high = guess - 1
        elif feedback == 'L' or feedback == 'l':
            low = guess + 1
    
    print(f"YAY! I Guessed Your Number HUMAN!")

guess(10)
print("Your Turn Human, it Better be Challenging!")
AI_Guess(100)    
