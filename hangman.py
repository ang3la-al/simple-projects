word = input("Get your friend to input a word: ")

allowed_errors = 8
# store letters guessed
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print("")
    done = True

    guess = input(f"Allowed errors remaining: {allowed_errors}, Next guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word -> {word}")
else:
    print(f"Game Over! The word was {word}")