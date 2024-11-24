import random

# random module from w3 schools can give more information about random module
#magic 8 ball

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ''
if fortune_number == 1:
    fortune_text = 'You will find your best friend today! Adopt a dog from your local shelter!'
if fortune_number == 2:
    fortune_text = 'A see fur and paws in your future. A dog is waiting for you at the shelter!'
if fortune_number== 3:
    fortune_text = 'You will adopt the best dog! Go visit the shelter today!'

print(f'{fortune_text} The number of dogs you should adopt today is {lucky_number}')
