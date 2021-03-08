import random

# This class determines our dices rolls, which dictate various outcomes.

class Dice(int):
    def __new__(self, sides=100):
        self.sides=sides
        self.value=self.getValue(self)
        self.values=[]
        return super(self, self).__new__(self, self.value)

    def getValue(self):
        return random.randrange(self.sides)+1
        return x

    def __repr__(self):
        return str(self.value)

    def __mul__(self, other):
        self.values=[]
        for die in range(other):
            self.values.append(self.getValue() )
        self.value = sum(self.values)
        return self

    __rmul__ = __mul__

    def highest(self, num):
        self.values.sort()
        print(self.values)
        self.value = sum(self.values[-num:])
        return self
    
    def lowest(self, num):
        self.values.sort()
        print(self.values)
        self.value = sum(self.values[:num])
        return self

# This class defines the player's Character and his various attributes

class Character (object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.maxHealth = 100
        attackRoll = 3*Dice(6)
        self.attack = attackRoll.highest(2).value
        defenseRoll = 3*Dice(6)
        self.defense = defenseRoll.highest(2).value
        self.morale = 3

# This class defines the Goblins, a hostile race which can be encountered in the dungeon.

class Goblin (object):
    def __init__(self):
        healthRoll = 6*Dice(10)
        healthValue = healthRoll.highest(5).value
        self.health = healthValue
        self.maxHealth = healthValue
        if healthValue > 40:
            self.name = "Goblin Chieftain"
            self.description = "Strong foe"
            self.aggression = 10
            self.morale = 3
            
        elif healthValue > 25:
            self.name = "Goblin Warrior"
            self.description = "Average foe"
            self.aggression = 8
            self.morale = 2
        else:
            self.name = "Wild Goblin"
            self.description = "Weak foe"
            self.aggression = 2
            self.morale = 1
        attackRoll = 3*Dice(6)
        self.attack = attackRoll.highest(2).value
        defenseRoll = 3*Dice(6)
        self.defense = defenseRoll.highest(2).value


class Dungeon(object):
    def __init__(self):
        pass

class City(object):
    def __init__(self):
        pass

class Room(object):
    def __init__(self):
        pass

# This class defines a series of commands, such as choosing a name for a character and the Exit function.

class Game (object):
    def __init__(self):
        self.character = None
        self.exit = False

    def run(self):
        while not self.exit:
            if not self.character:
                name = input("Choose your name \n>>>")
                name = name.strip()
                testName = name.replace(" ", "")
                if not testName.isalpha():
                    print("Warning: Your name can only contain alphabetic characters.")
                    continue

                self.character = Character(name)

            cmd = input("{0} HP:{1}/{2} ATT:{3} DEF:{4}>>>".format(self.character.name, self.character.health,self.character.maxHealth, self.character.attack, self.character.defense))

            cmd = cmd.strip()

            if cmd.lower() == "exit":
                self.exit = True
            else:
                print("Warning: Command is not recognized.")

            print("\n")

Game().run()
