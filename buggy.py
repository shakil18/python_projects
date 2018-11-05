import random

number1 = random.randint (1,10)
number2 = random.randint (1,10)
print('What is ' + str(number1) + ' + ' + str(number2))
answer = input()
number3 = number1+number2
if answer == number1 + number2:
    print('Correct!')

else:
    print('Nope! The answer is ' + number3)
