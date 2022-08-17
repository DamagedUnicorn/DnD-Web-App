#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:25:57 2022

@author: thorknudsen
"""

class Weapon:
    def __init__(self):
        #self.isProficient = False
        pass

    def setName(self, name):
        self.name = name

    #def setDamage(self, die, numberOfDice):
    #    self.die = die
    #    self.numberOfDice = numberOfDice

    def setType(self, Type):
        self.Type = Type

    def setProperties(self, properties):
        self.properties = properties

    def isWeaponProficient(self, data):
        self.isProficient = False
        simpleWeaponList = ["Club", "Dagger", "Greatclub", "Handaxe", "Javellin", 
                            "Light-hammer", "Mace", "Quarterstaff", "Sickle", "spear", 
                            "Crossbow, light", "Dart", "Shortbow", "Sling"]
        martialWeaponList = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", 
                             "Halberd", "Lance", "Longsword", "Maul", "Morningstar", 
                             "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", 
                             "War-pick", "Warhammer", "Whip", "Blowgun", "Crossbow, hand", 
                             "Crossbow, heavy", "Longbow", "Net"]

        for key, item in data.get("modifiers").items():
            for val in item:
                if val.get("type") == "proficiency":
                    if val.get("subType") == "simple-weapons":
                        if self.Type in simpleWeaponList:
                            self.isProficient = True
                    elif val.get("subType") == "martial-weapons":
                        if self.Type in martialWeaponList:
                            self.isProficient = True
                    elif val.get("subType") == self.Type:
                        self.isProficient = True


        

        