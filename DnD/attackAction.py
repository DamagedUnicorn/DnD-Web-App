class AttackAction:
    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def setDamage(self, diceAmount, diceType, diceString):
        self.diceAmount = diceAmount
        self.diceType = diceType
        self.diceString = diceString
