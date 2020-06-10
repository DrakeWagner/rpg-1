from random import randint


#### Test Player
class Player_Class_Combat_Tests:
    def __init__(self, myclass=None, hp=200, strength=5, agility=5, gold=0):
        self.myclass = myclass
        self.hp = hp
        self.strength = strength
        self.agility = agility
        self.gold = gold


p5 = Player_Class_Combat_Tests()
print(p5)


####
# Classes
class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhp = 20
        self.hp = self.maxhp
        self.attack = 5
        self.agility = 1


test_zombie = Zombie('test_zombie')
print(test_zombie)


class Skeleton:
    def __init__(self, name):
        self.name = name
        self.maxhp = 15
        self.hp = self.maxhp
        self.attack = 3
        self.agility = 3


test_skeleton = Skeleton('test_skeleton')
print(test_skeleton)


# Decides the enemy
def enemy_decider():
    enemy = None
    num = randint(1, 2)
    if num == 1:
        enemy = test_skeleton
    elif num == 2:
        enemy = test_zombie
    print('A {} suddenly appears!'.format(enemy.name))
    # fight()


enemy_decider()


def fight():
    global enemy
    while enemy.hp > 0 | p1.hp > o:
        print('1) Attack')
        print('2) Run')
        option = input('')
    if option == '1':
        attack()
    if option == '2':
        run()
