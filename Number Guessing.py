#Computing game
import random
number = random.randint(1, 50)

player_name = input("Hello, What's your name? ")
number_of_guesses = 0
print('Hello, '+ player_name+ ' I am Guessing a number between 1 and 50, write your guess below, and press enter:')

while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
