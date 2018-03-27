from random import randint


guesses_taken = 0
number = randint(1, 11)

while guesses_taken < 5:
    print("Guess a number between 1 and 10")
    guesses_taken = guesses_taken + 1
    guess = input()
    if guess.isdigit():
        if int(guess) == number:
            break
        elif int(guess) > number:
            print('your guess is too high!')
        elif int(guess) < number:
            print('your guess is too low!')
    else:
        print("Your guess must be a positive whole number")

if number == input():
    guesses_taken = str(guesses_taken)
    print('Good job! You guessed the number in ' + guesses_taken + 'guesses!')
if number != input():
    number = str(number)
    print('Sorry, the number is ' + number)