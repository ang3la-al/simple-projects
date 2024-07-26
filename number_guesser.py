import random

def get_upper_boundary():
    while True:
        upper_boundary = input("Pick a number: ")
        if upper_boundary.isdigit():
            upper_boundary = int(upper_boundary)
            if upper_boundary > 0:
                return upper_boundary
            else:
                print("Please pick a number greater than 0.")
        else:
            print("Please type a valid integer.")

upper_boundary = get_upper_boundary()
random_number = random.randint(1, upper_boundary)
total_guesses = 0

while True:
    total_guesses += 1
    user_input = input(f"Guess a number between 1 and {upper_boundary}: ")
    if user_input.isdigit():
        guess = int(user_input)
    else:
        print("Please input a valid integer")
        continue

    if guess == random_number:
        print("Well done, you got it!")
        break
    elif guess > random_number:
        print("Too high!")
    else:
        print("Too low!")

print("You got it in " + str(total_guesses) + " guesses")