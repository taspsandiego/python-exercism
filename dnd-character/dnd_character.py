import random
import math

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()                   
        self.hitpoints = 10 + modifier(self.constitution)        

    def ability(self):
        die = []
        for i in range(4):
            die.append(random.randint(1,6))
        die.sort()
        return sum(die[1:4])


def modifier(constitution):
    return math.floor((constitution - 10)/2.0) 



