#def choose_gesture
#user chooses from 5 options and updates active_gesture
from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        print(f' {self.name}, select your move: ')
        for x in range(len(self.gestures)):
            print(f'{x} for {self.gestures[x]}')
        choice = int(input())
        self.active_gesture = self.gestures[choice]