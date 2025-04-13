import random



number = random.randint(1,100)
while True:
    guess = int(input("Enter Your Guess Number : "))
    if guess < number:
        print("To Low Number!")
    elif guess > number:
        print("To High Number!")  
    else:
        print("You Got It Right")  
        break


