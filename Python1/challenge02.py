'''write a Python program that generates a random secret number between 1 and 100.
 The user must guess the number. After each guess, the program should tell them if their guess is "too high", "too low", or "correct".
 The game should continue until the user guesses the correct number, and then print how many attempts it took.
 Hint: Use the random module for number generation and a while loop for repeated guesses.'''
import random
secret_number=random.randint(1,100)
attempt=0
guess=0

print("Am thinking of num between 1 to 100!!")
while guess != secret_number:
    try:
        guess_input= input("Enter num between 1 to 100")
        guess=int(guess_input)
        attempt += 1
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("too high")
        else :
            print(f"correct you guessed in {attempt} attempts")
    except ValueError:
        print("Error")
    