from game import Game

#create game
#run game
#ask if player wants to play again 

game = Game()
game.run_game()
user_input = ''
while user_input != 'y' and user_input != 'n':
    user_input = input('Do you want to play again? Enter y or n')
    if user_input == 'y':
        game.run_game()
    elif user_input == 'n':
        break
    else:
        print('Error')
