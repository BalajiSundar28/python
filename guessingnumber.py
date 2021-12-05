import random
guess=int(input('enter guessing number'))
hidden=random.randint(1,100)
if guess==hidden:
	print('you guessed the right number')
else:
	print('sorry, you guessed the wrong number')
	print('hidden number is',hidden)
