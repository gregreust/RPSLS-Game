#def choose_gesture
#random choice from gesture list becomes active gesture
from player import Player
from random import choice

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.active_gesture = choice(self.gestures)
