import random

def guess_number_game():
    number_to_guess = random.randint(0,1000)
    print("I've picked a number between 0 and 1000. Try to guess that number! 500")
    
    while True:
        try:
            guess = int(input("Your guess"))
        except ValueError:
            print("Enter an accepted number between 0 and 1000") 
            continue
        
        if guess < number_to_guess:
            print("Your chosen number is to small ")
            print("Enter a new, bigger number ")
        elif guess > number_to_guess:
            print("Your chosen number is to big ")
            print("Enter a new, smaller number ")
        else:
            print("You chose the correct number!", number_to_guess)
            break

guess_number_game()
        