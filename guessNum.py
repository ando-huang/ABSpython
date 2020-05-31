import random

i = random.randint(1, 10)

print("Hi, guess a number!")

int_guess = 0
count = 1
while int_guess != i:

    int_guess = int(input())

    if int(int_guess) == i:
        print("You got it!")
        exit()
    elif int(int_guess) < i:
        print("too low!")
    else:
        print("too high!")
    print("You've taken " + str(count) + " guesses!")
    print("Guess again!")
    count += 1
