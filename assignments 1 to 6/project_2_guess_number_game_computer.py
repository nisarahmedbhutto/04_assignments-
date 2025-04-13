# guess the number game by computer

import random 

def guess_number():
    """
        project 2 : guess the number game by computer.
    """
    number = random.randint(1,100)
    guesses_left = 10

    # wellcome  

    print("Wellcome to the number guessing game ")
    print("I am thinking a number between 1 to 100")

    # loop generate
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess of number."))
        except ValueError:

            print("Invalid input : Please enter a number.")
            continue
        if guess < number:
            print("Too low number . Tell anouther!")
        elif guess > number:
            print("Too high number . Tell anouther!")
        else:
            print(f"Congratulation! you got the correct number in {10 - guesses_left + 1} tries")
            return
        
        guesses_left -= 1


        # guess finished 
        print(f"\n You ran out of guess . The number was {number}.")


guess_number()


        