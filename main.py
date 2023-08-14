# Created by Alycia Febriana

import random

def play():
    print("Welcome to Number Guessing Game!")
    name = input("\nEnter your name : ")
    
    random_number = random.randint(1,100)
    attempt = 0
    max_attempt = 10
    
    print(f"\nHello {name}! Guess a number between 1 and 100")
    print(f"There are {max_attempt} attempts")
    
    while attempt < max_attempt:
        guess = int(input("\nYour guess is "))
        
        if guess < 1 or guess > 100:
            print("Please enter a guess between 1 and 100")
            continue
        
        attempt += 1
        
        if guess < random_number:
            print("Number is too low")
        elif guess > random_number:
            print("Number is too high")
        else:
            print(f"\nCongratulations {name}! You've guessed it right")
            break
    
    if attempt >= max_attempt:
        print("\nSorry, you've reached max attempts")
    
    again = input("Do you want to play again? ").lower()
    while again not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'")
        again = input("Do you want to play again? ").lower()
        
    if again == "yes":
        play()
    else:
        print("\nThank you for playing")
        
play()