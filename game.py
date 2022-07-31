from player import Player
from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player_1 = Player('Player 1')
        self.player_2 = Player('Player 2')
        self.turn_counter = 1


#def Intro. Do you want to see the rules? 
#if yes, display rules
    def intro(self):
        print('')
        self.turn_counter = 0               #need to reset this if user plays again 
        print('It\'s time for rock, paper, scissors, lizard, Spock.')
        user_input = ''
        while user_input != 'y' and user_input != 'n':
            user_input = input('Do you want to see the rules? Enter y or n').lower()
            if user_input == 'y':
                print('')
                print('Best 2 out of 3')
                print('Scissors cuts paper, paper covers rock,')
                print('rock crushes lizard, lizard poisons Spock,')
                print('Spock smashes scissors, scissors decapitates lizard,')
                print('lizard eats paper, papers disproves Spock,')
                print('Spock vaporizes rock, and as it always has, rock crushes scissors.')
            elif user_input == 'n':
                break
            else:
                print('Error.')

    def choose_players(self):
        print('')
        user_input = ''
        while user_input != '1' and user_input != '2' and user_input != '3':
            user_input = input('Enter 1 for one player, 2 for two players, or 3 to spectate').lower()
            if user_input == '1':
                self.player_1 = Human('Player 1')
                self.player_2 = Ai('Player 2')
            elif user_input == '2':
                self.player_1 = Human('Player 1')
                self.player_2 = Human('Player 2')
            elif user_input == '3':
                self.player_1 = Ai('Player 1')
                self.player_2 = Ai('Player 2')
            else:    
                print('Error.')

#def one_round
#player 1 select gesture
#player 2 select gesture
#compare gesture and declare winner

    def one_round(self):
        self.player_1.choose_gesture()
        self.player_2.choose_gesture()
        print('')
        print(f'{self.player_1.name} used {self.player_1.active_gesture}')
        print(f'{self.player_2.name} used {self.player_2.active_gesture}')
        winner = self.compare_gesture()
        self.turn_counter += 1
        if self.player_1.win_counter < 2 and self.player_2.win_counter < 2:
            print(f'{winner} Get ready for round {self.turn_counter}')
        else:
            return


#def compare_gesture
#if xxxx and xxxx then add to win counter return winner or tie 
#technically, I could replace the 5 tied cases with one if statement

    def compare_gesture(self):
        print('')
        if self.player_1.active_gesture == 'rock' and self.player_2.active_gesture == 'rock':
            return 'This one was a tie.'
        elif self.player_1.active_gesture == 'rock' and self.player_2.active_gesture == 'paper':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'rock' and self.player_2.active_gesture == 'scissors':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'rock' and self.player_2.active_gesture == 'lizard':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'rock' and self.player_2.active_gesture == 'Spock':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'paper' and self.player_2.active_gesture == 'rock':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'paper' and self.player_2.active_gesture == 'paper':
            return 'This one was a tie.'
        elif self.player_1.active_gesture == 'paper' and self.player_2.active_gesture == 'scissors':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'paper' and self.player_2.active_gesture == 'lizard':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'paper' and self.player_2.active_gesture == 'Spock':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'scissors' and self.player_2.active_gesture == 'rock':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'scissors' and self.player_2.active_gesture == 'paper':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'scissors' and self.player_2.active_gesture == 'scissors':
            return 'This one was a tie.'
        elif self.player_1.active_gesture == 'scissors' and self.player_2.active_gesture == 'lizard':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'scissors' and self.player_2.active_gesture == 'Spock':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'lizard' and self.player_2.active_gesture == 'rock':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'lizard' and self.player_2.active_gesture == 'paper':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'lizard' and self.player_2.active_gesture == 'scissors':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'lizard' and self.player_2.active_gesture == 'lizard':
            return 'This one was a tie.'
        elif self.player_1.active_gesture == 'lizard' and self.player_2.active_gesture == 'Spock':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'Spock' and self.player_2.active_gesture == 'rock':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'Spock' and self.player_2.active_gesture == 'paper':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'Spock' and self.player_2.active_gesture == 'scissors':
            self.player_1.win_counter += 1
            return f'{self.player_1.name} wins!'
        elif self.player_1.active_gesture == 'Spock' and self.player_2.active_gesture == 'lizard':
            self.player_2.win_counter += 1
            return f'{self.player_2.name} wins!'
        elif self.player_1.active_gesture == 'Spock' and self.player_2.active_gesture == 'Spock':
            return 'This one is a tie'
        

#def run_game
#intro
#choose 1 player or 2 player game (or ai vs ai)
#loop one_round until one player wins twice
#declare final winner 

    def run_game(self):
        self.intro()
        self.choose_players()
        while self.player_1.win_counter < 2 and self.player_2.win_counter < 2:
            self.one_round()
        print('')
        if self.player_1.win_counter > self.player_2.win_counter:
            print(f'Congratulations to {self.player_1.name} for winning 2 out of 3!')
        else:
            print(f'Congratulations to {self.player_2.name} for winning 2 out of 3!')