print('welcome to my computer quiz!')

playing  =  input("DO you want to play? ")
if playing.lower() != 'yes':
    quit()

print("okay! lets play :)")

score = 0

answer =  input('What does CPU stand for? ')
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Sorry incorrect answer')

answer =  input('What does GPU stand for? ')
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print('Sorry incorrect answer')

answer =  input('What does RAM stand for?  ')
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print('Sorry incorrect answer')

print()
print('congrats, your score is {}'.format(score))
print(f'your percentage is {(score/3) * 100} %')
