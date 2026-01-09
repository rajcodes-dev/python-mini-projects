# A Rock-Paper-Scissor Game 
import random
print("----- Welcome to the game -----")
run = True

while(run):
    moves = ['Rock','Paper','Scissor']
    computer_move = random.choice(moves)
    user_move = input('\nRock!! Paper!! Scissor!!\nYour move:\n')

    computer_move = computer_move.strip().lower()
    user_move = user_move.strip().lower()
    
    if user_move == computer_move:
        print("\nOponent Move:\n",computer_move)
        print('Tie')

    elif user_move == 'rock' and computer_move == 'scissor':
        print("\nOponent Move:\n",computer_move)
        print("You Win!")

    elif user_move == 'rock' and computer_move == 'paper':
        print("\nOponent Move:\n",computer_move)
        print("You Lose!")

    elif user_move == 'paper' and computer_move == 'scissor':
        print("\nOponent Move:\n",computer_move)
        print("You Lose!")

    elif user_move == 'paper' and computer_move == 'rock':
        print("\nOponent Move:\n",computer_move)
        print("You Win!")

    elif user_move == 'scissor' and computer_move == 'paper':
        print("\nOponent Move:\n",computer_move)
        print("You Win!")

    elif user_move == 'scissor' and computer_move == 'rock':
        print("\nOponent Move:\n",computer_move)
        print("You Lose!")

    else:
        print('\nInvalid Move!')

    choice = input("\nDo you want to play again(y/n):")
    if choice == 'n':
        run = False
