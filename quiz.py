playing_status = input("Welcome to the computer quiz! Would you like to play? Yes or No. ")

if playing_status.lower() != "yes":
    print("See you next time!")
    quit()

print("Great! Let's begin! ")

points = 0
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    points += 1
    print("Correct! You have " + str(points) + " point(s)")
else:
    print("Incorrect! The answer was Random Access Memory.")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    points += 1
    print("Correct! You have " + str(points) + " point(s)")
else:
    print("Incorrect! The answer was Central Processing Unit.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    points += 1
    print("Correct! You have " + str(points) + " point(s)")
else:
    print("Incorrect! The answer was Graphics Processing Unit.")

print("Thanks for playing, your total score was: " + str(points))