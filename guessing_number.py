import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('please enter a number greater than 0')
        quit()
else:
    print("Please enter a number next time")
    quit()


random_number = random.randint(0,top_of_range)
guess = 0
while True:
    guess += 1
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please enter a number next time')
        continue

    if user_guess == random_number:
        print('congrats you got it right :)')
        break
    elif user_guess > random_number:
        print('your guess is greater than the actual value')
    else:
        print('your guess is less than the actual value')
print(f"You got it in the {guess} guesses")
