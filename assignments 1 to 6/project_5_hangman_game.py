import random


words = ["enum","python","colab","javascript","java"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Wellcome To Hangman Game Project 8 ")
print("_ " * len(word))

while attempts > 0:
    guess = input("\n Guess The Letters : ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Write One Alphabat Only!")
        continue
    if guess in guessed_letters:
        print("this letter is already guess choose another letter ")
        continue

    if guess in word:
        print("Correct Guess! ")
    else:
        attempts -= 1
        print(f"Wrong {attempts} Attempts.")
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(display_word)

    if "_" not in display_word:
        print(f"Congratulation! the correct word is : {word}")
        break
else:
    print(f"Game Over! The Correct Word Is : {word}")