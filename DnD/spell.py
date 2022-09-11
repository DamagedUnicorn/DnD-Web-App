#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:25:57 2022

@author: thorknudsen
"""


from statistics import mode


class Spell:
    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def setDamage(self, die, numberOfDice, diceString):
        self.die = die
        self.numberOfDice = numberOfDice
        self.diceString = diceString

    def setToHitBonus(self, Class, modifiers, proficiencyBonus):
        if Class in ["Artificer", "Fighter", "Rogue", "Wizard"]:
            bonus = modifiers[3] + proficiencyBonus
        elif Class in ["Cleric", "Druid", "Monk", "Ranger"]:
            bonus = modifiers[4] + proficiencyBonus
        else:
            bonus = modifiers[5] + proficiencyBonus

        self.toHitBonus = bonus

    def setDamageBonus(self, Class, modifiers):
        if Class in ["Artificer", "Fighter", "Rogue", "Wizard"]:
            bonus = modifiers[3]
        elif Class in ["Cleric", "Druid", "Monk", "Ranger"]:
            bonus = modifiers[4]
        else:
            bonus = modifiers[5]

        self.damageBonus = bonus
