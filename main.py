import random

print('Let play rock paper scissors')
myAnswer = input()


options = ['rock', 'paper', 'scissors']

rando = random.choice(options)
print(rando)

if rando == myAnswer:
  print('Oh no! Its a tie. Lets play again')
elif myAnswer == 'rock' and rando == 'scissors':
  print('You win :(')
elif myAnswer == 'paper' and rando == 'scissors':
  print('Haha I win :)')
elif myAnswer == 'rock' and rando == 'paper':
    print('Haha I win :)')
elif myAnswer == 'scissors' and rando == 'paper':
    print('You win :(')
elif myAnswer == 'paper' and rando == 'rock':
    print('You win :(')
elif myAnswer == 'scissors' and rando == 'rock':
    print('Haha I win :)')
