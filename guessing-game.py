import random

maxTurns=5
lowerBound=1
upperBound=20

def get_player_name():
    return input('What is your name? ')

def choice_play_game(invitation):
    while True:
        play=input(invitation).upper()
        if play.isspace() or  play == '' or play.upper() == 'Y':
            return True
        elif play.upper() == 'N':
            return False
        else:
            print('I didn\'t understand you. Be more clear.\n')

def guess_get():
    validGuess = False
    while not validGuess:
        guess = input('What is your guess? ')
        if guess.isnumeric():
            guess = int(guess)
            if guess < lowerBound or guess > upperBound:
                print('You need to pick an integer between ' + \
                      str(lowerBound) + ' and ' + str(upperBound) + ' inclusive. Silly.\n')
            else:
                validGuess = True
        else:
            print('You need to pick an integer. Silly.\n')
    return guess

def guess_check(guess, target):
    if guess == target:
        return 0
    elif guess < target:
        return -1
    else:
        return 1

player1 = get_player_name()

print('Well ' + player1 + ', I am thinking of an integer between ' + \
      str(lowerBound) + ' and ' + str(upperBound) + ' inclusive.\n\n' + \
      'The game is that you try to guess the number in ' + str(maxTurns) + '.\n')

challenge = 'Does this sound like fun? ([y]/n): '
playGame=choice_play_game(challenge)
while playGame:
    # Initialize the game
    target = random.randint(1,20)               # Pick the target number
    cTurn = 1                                   # Increment the turn
    check = 100                                 # Pick a bad number
    winner = ''                                 # There's no winner yet
    while cTurn <= maxTurns and winner == '':
        guess=guess_get()
        check = guess_check(guess, target)
        if check == -1:
            response = 'Your guess is too low. You have ' + \
                       str(maxTurns - cTurn) + ' turns left.'
        elif check == 1:
            response = 'Your guess is too high. You have ' + \
                       str(maxTurns - cTurn) + ' turns left.'
        elif check == 0:
            response = 'You got it in only ' + str(cTurn) + '! ' + \
                       'I guess humans are smarter than I thought.'
            winner = 'Human'
        else:
            response = 'ERROR: Bad check function response\n'
        print(response)
        if winner != '':
            break
        else:
            cTurn += 1
    else:
        print('You didn\'t guess the number in ' + str(maxTurns) + \
              ', so I win. Hah! Computers rule!!!!')
        winner = 'Computer'
    if winner == 'Computer':
        challenge = 'Well, is your feeble intellect up for another beating? ([y]/n): '
        playGame=choice_play_game(challenge)
    else:
        challenge = 'Well, would you be willing to give me another chance? ([y]/n): '
        playGame=choice_play_game(challenge)
else:
    print('Ok, maybe later.\n')
