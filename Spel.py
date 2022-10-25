import time


def clear():
    pass


class Monster():
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg


class Spelare():
    def __init__(self, namn):
        self.namn = namn
        self.hp = 50
        self.dmg = 10
        self.pengar = 0
        self.ryggsäck = []

# Starten på den fantastiska resan


namn = input("Hej, Vad vill du bli kallad? --> ")
spelare = Spelare(namn)

# hej
print("ASASASA")
