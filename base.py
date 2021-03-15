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
        self.weapon = None

    def fight(self, goblin):
        attack = Dice(self.attack)
        defense = Dice(goblin.defense)
        goblin.aggression = 10

        if not self.weapon:
            if defense > attack:
                print("\n")
                print("You take a swing at the {0}, but it evades the attack and prepares to retaliate".format (goblin.name.lower()))
                print("\n")

            elif attack == defense: 
                print("\n")
                print("You slash the {0}, although its armor absorbs some of the damage".format (goblin.name.lower()))
                print("\n")
                goblin.health -= attack/2
            
            elif attack > defense:
                print("\n")
                print("You deliver a staggering blow as the {0} lets out a loud shriek".format (goblin.name.lower()))
                print("\n")
                goblin.health -= attack

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

    def fight(self, player):
        attack = Dice(self.attack)
        defense = Dice(player.defense)

        if defense > attack:
            print("\n")
            print("The {0} takes a swing at you but you manage to dodge the attack, thus taking no damage".format (self.name.lower()))
            print("\n")

        elif attack == defense: 
            print("\n")
            print("You skilfully block the strike, but still receive some damage as the {0} swipes at you".format (self.name.lower()))
            print("\n")
            player.health -= attack/2
        
        elif attack > defense:
            print("\n")
            print("The {0} strikes you with a crushing blow, tearing through your defenses".format (self.name.lower()))
            print("\n")
            player.health -= attack



class Room(object):
    def __init__(self):
        self.name="Room Name"
        self.description="Room Description"
        self.exits=[]
        self.goblins=[]


def dungeon():
    while True:
        room = Room()

        room.name = "Dark Cave"
        cavesizeRoll = random.randint(0,3)
        if cavesizeRoll == 0:
            cavesize = " a very dark and cramped maze which you find difficult to maneuver"
        elif cavesizeRoll == 1:
            cavesize = "a narrow cave. You cannot see much, but you have enough room to move around"
        elif cavesizeRoll == 2:
            cavesize = "a long open corridor of rock and crystals"
        else:
            cavesize = "a massive wide-open geode that you are standing inside of"

        wetnessRoll = random.randint(0,3)
        if wetnessRoll == 0:
            wetness = "the air is dry as you can hear the clicks of your heels against the rock below"
        elif wetnessRoll == 1:
            wetness = "the air is a little damp as you can smell the must and the mildew"
        elif wetnessRoll == 2:
            wetness = "it is very damp as you can see water seeping through the walls of the cave"
        else:
            wetness = "you are soaking wet since the cave system is nearly flooded in this part"

        exitRoll = random.randint(0,3)
        if exitRoll == 0:
            room.exits.append("north")
        elif exitRoll == 1:
            room.exits.append("west")
        elif exitRoll == 2:
            room.exits.append("south")
        else:
            room.exits.append("east")

        room.description = "This part of the cave is {0} and {1}.\n\nExits: {2}".format(cavesize,wetness, ", ".join(room.exits))

        goblinRoll = random.randint(0,4)
        if goblinRoll == 0:
            pass
        elif goblinRoll == 1:
            room.goblins.append(Goblin())
        elif goblinRoll == 2:
            room.goblins.append(Goblin())
        elif goblinRoll == 3:
            room.goblins.append(Goblin())
        else:
            room.goblins.append(Goblin())
            room.goblins.append(Goblin())

    
        yield room
 



# This class defines a series of commands, such as choosing a name for a character and the Exit function.

class Game (object):
    def __init__(self):
        self.character = None
        self.exit = False
        self.room = None
        self.dungeon = dungeon()

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

            if not self.room:
                self.home()
                continue

            self.look()
            self.combat()
            self.cleanup()
            print("\n")

            if not self.character: 
                self.room = None
                continue


            cmd = input("{0} HP:{1}/{2} ATT:{3} DEF:{4}>>>".format(self.character.name, self.character.health,self.character.maxHealth, self.character.attack, self.character.defense))

            cmd = cmd.strip()

            if cmd.lower() == "exit":
                self.exit = True
            elif cmd.lower() in self.room.exits:
                self.room = next(self.dungeon)
            elif cmd.lower() == "kill goblin" or cmd.lower() == "attack goblin":
                if self.room.goblins:
                    self.character.fight (self.room.goblins[0])
                else:
                    print("\n")
                    print("There are no goblins around")
                    print("\n")
            elif cmd.lower() == "look":
                continue

            else:
                print("Warning: Command is not recognized.")

            print("\n")

    def combat(self):
        for goblin in self.room.goblins:
            if goblin.aggression == 10:
                goblin.fight(self.character)
                self.character.fight(goblin)
            elif goblin.aggression > 4:
                coinFlip = random.randint(0, 1)
                if coinFlip:
                    goblin.fight(self.character)
                    goblin.aggression = 10
                    self.character.fight(goblin)

    def cleanup(self):
        # Player Death
        if self.character.health < 1:
            print("\n")
            print("YOU DIED")
            print("\n")
            print("Game Over")
            print("\n")
            self.character = None
            return

        # Goblin Death
        livingGoblins = []
        for goblin in self.room.goblins:
            if goblin.health < 1:
                if not self.character.weapon:
                    print("\n")
                    print("The {0} lets out one final shriek before it falls dead to the ground".format(goblin.name.lower()))
                    print("\n")
            else:
                livingGoblins.append(goblin)
        self.room.goblins = livingGoblins
            

    def look(self):
        print("\n\n")
        print(self.room.name)
        print("\n\n")
        print(self.room.description)
        if self.room.goblins:
            print("\n")
            print("Goblins:{0}".format(", ".join([g.name for g in self.room.goblins])))
        print("\n")
    def home(self):
        homeRoom = Room()
        homeRoom.name = "Great Hall"
        homeRoom.description = "You are in your great hall, a safe place where you can rest, heal and ressuply. To the south, you can see a doorway that leads into an unexplored labyrinth of caves and eerie tunnels. Above the doorway lay an inscription, but you cannot make sense of the markings.\n\nExits: south"
        homeRoom.exits = ["south"]
        self.room = homeRoom



Game().run()
