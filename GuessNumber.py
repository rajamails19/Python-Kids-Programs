import random

def guess_number():
    secret = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10!")
    
    while True:
        guess = int(input("What's your guess? "))
        if guess == secret:
            print("Wow! You got it right! 🎉")
            break
        elif guess < secret:
            print("Too low! Try again! ⬆️")
        else:
            print("Too high! Try again! ⬇️")
