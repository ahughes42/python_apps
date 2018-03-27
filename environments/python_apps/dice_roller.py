from random import randint

def dice_roll():
    print("Would you like to roll? ")
    answer = input()
    while answer == "yes" or answer == 'y':
        num1 = randint(1, 6)
        num2 = randint(1, 6)
        total = num1 + num2
        print("You rolled ", num1, "& ", num2, "For a total of ", total)
        if num1 == num2:
            print("You rolled doubles!")
        print("Would you like to roll again?")
        answer = input()
    else:
        print("Come back soon!")

dice_roll()