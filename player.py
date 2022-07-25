#has a list of gestures
#has an active gesture
#has a counter for number of wins
class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
        self.active_gesture = 'rock'
        self.win_counter = 0
