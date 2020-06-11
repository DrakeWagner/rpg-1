from random import randint


#### Test Player
class Player_Class_Combat_Tests:
    def __init__(self, myclass=None, hp=200, maxhp=40, strength=5, agility=5, gold=0):
        self.myclass = myclass
        self.hp = hp
        self.maxhp = maxhp
        self.strength = strength
        self.agility = agility
        self.gold = gold


p5 = Player_Class_Combat_Tests()
player = p5
print(p5)


####
# Classes
class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhp = 20
        self.hp = self.maxhp
        self.strength = 5
        self.agility = 1


test_zombie = Zombie('test_zombie')
print(test_zombie)


class Skeleton:
    def __init__(self, name):
        self.name = name
        self.maxhp = 15
        self.hp = self.maxhp
        self.strength = 3
        self.agility = 3


test_skeleton = Skeleton('test_skeleton')
print(test_skeleton)

enemy = None


# Decides the enemy
def enemy_decider():
    global enemy
    num = randint(1, 2)
    if num == 1:
        enemy = test_skeleton
    elif num == 2:
        enemy = test_zombie
    print('A {} suddenly appears!'.format(enemy.name))


# Turn based fighting
def Player_Attack(player, enemy):
    damage = player.strength + randint(-2, 2)
    enemy.hp -= damage
    print('You attack the {} for {} damage.'.format(enemy.name, damage))


def enemy_attack(player, enemy):
    damage = enemy.strength + randint(-2, 2)
    player.hp -= damage
    print('The {} hit you for {} damage!'.format(enemy.name, damage))


def attack(player, enemy):
    # Your attack
    damage = player.strength + randint(-2, 2)
    enemy.hp -= damage
    print('You attack the {} for {} damage.'.format(enemy.name, damage))
    # their attack
    damage = enemy.strength + randint(-2, 2)
    player.hp -= damage
    print('The {} hit you for {} damage!'.format(enemy.name, damage))


def fight():

    enemy_decider()
    global enemy

    while p5.hp > 0 | enemy.hp > 0:
        print('1) Attack')
        print('2) Run')
        option = input('>>> ')
        if option == '1':
            attack(player, enemy)
            print('')
            if player.hp > 0:
                print('Your hp: {}/{}'.format(p5.hp, p5.maxhp))
            elif player.hp <= 0:
                print('Oh dear, you died.')
            if enemy.hp > 0:
                print('{} hp: {}/{}'.format(enemy.name, enemy.hp, enemy.maxhp))
            elif enemy.hp <= 0:
                print('You killed the {}!'.format(enemy.name))

        if option == '2':
            pass

fight()
