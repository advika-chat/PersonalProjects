import random
print ('Choose a number from the following: \n1) ✊\n2) ✋\n3) ✌️')
player = int(input('Pick a number: '))

computer = random.randint(0,3)

dict = {
  1: "✊",
  2: "✋",
  3: '✌️'
}

print(f'You chose: {dict[player]}')
print(f'Computer chose: {dict[computer]}')

win = {
    1: 3,
    2: 1,
    3: 2
}

if (player == computer):
    print('It\'s a tie!')
elif (win[player] == computer):
    print ('You win!')
else:
    print ('Computer wins :(')