class Player:
    def __init__(self, name):
        self.name = name
        self.wisdom = 0
        self.courage = 0
        self.selflessness = 0
        self.strength = 0

    def gain_wisdom(self, amount):
        self.wisdom += amount

    def gain_courage(self, amount):
        self.courage += amount

    def gain_selflessness(self, amount):
        self.selflessness += amount

    def gain_strength(self, amount):
        self.strength += amount

class Quest:
    def __init__(self, name, challenge, reward):
        self.name = name
        self.challenge = challenge
        self.reward = reward

class Location:
    def __init__(self, name, quest):
        self.name = name
        self.quest = quest

class Boss:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


