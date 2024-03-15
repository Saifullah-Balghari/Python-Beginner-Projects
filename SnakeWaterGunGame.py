import random

comp_guess = random.randint(0, 2)
user_guess = int(input("Enter 0 for snake, 1 for water and 2 for gun:  "))


def check(comp_guess, user_guess):

    if comp_guess == user_guess:
        return 0
    if comp_guess == 1 and user_guess == 0:
        return 1
    if comp_guess == 2 and user_guess == 1:
        return 1
    if comp_guess == 0 and user_guess == 2:
        return 1


print("You: ", user_guess)
print("Computer: ", comp_guess)

score = check(comp_guess, user_guess)

if score == 0:
    print("It's draw.")
if score == 1:
    print("You won.")
else:
    print("You loose.")
