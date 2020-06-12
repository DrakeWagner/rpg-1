import sys
from random import randint

for i in range(0, 5):
    print(' ')
print('===================================================')
print('=========== Welcome to rpg_1_test =================')
print('===================================================')


def main_menu():
    print('Welcome to rpg_1_test!')
    print('1) Start')
    print('2) About')
    print('3) Exit')
    menu_input = input('>>> ')
    if menu_input == '1':
        start()
    if menu_input == '2':
        pass
    if menu_input == '3':
        sys.exit()
    else:
        main_menu()


class Player_Class:
    def __init__(self, myclass=None, hp=0, maxhp=30, strength=0, agility=0, gold=0):
        self.myclass = myclass
        self.hp = hp
        self.maxhp = maxhp
        self.strength = strength
        self.agility = agility
        self.gold = gold

    def pick_class(self):
        # Chooses the player's main class
        myclassOptions = ['warrior', 'wizard', 'archer']
        print('Create your player')
        print('You may pick from the options "warrior", "wizard", and "archer"')
        while True:
            myclasschoice = input('>>  ')
            if myclasschoice in myclassOptions:
                self.myclass = myclasschoice
                print('You have chosen {}!'.format(myclasschoice))
                break
            else:
                print('Please try again. Enter "warrior", "wizard", or "archer"')
        if self.myclass == 'warrior':
            self.maxhp = 25
            self.hp = 25
            self.strength = 3
            self.agility = 1
        if self.myclass == 'archer':
            self.hp = 15
            self.strength = 5
            self.agility = 3
        if self.myclass == 'wizard':
            self.hp = 10
            self.strength = 6
            self.agility = 2


# Assigns the chosen class to p1
p1 = Player_Class()


# Starts the game loop
def start():
    p1.pick_class()
    print(p1)
    menu(p1)


# Main loop of the game
def menu(your_player):

    print('================')
    print('Gold: %i' % your_player.gold)
    print('HP: %i' % your_player.hp)
    print(' ')
    print('1) Fight')
    print('2) Store')
    print('3) Player Info')
    print('4) Main Menu')
    option = int(input('>> '))
    if option == 1:
        fight()
    elif option == 2:
        store()
    elif option == 3:
        print(p1.__dict__)
        menu(p1)
    elif option == 4:
        main_menu()


# Classes
class Zombie:
    def __init__(self, name='Zombie'):
        self.name = name
        self.maxhp = 20
        self.hp = self.maxhp
        self.strength = 5
        self.agility = 1
        self.gold = randint(3, 5)


class Skeleton:
    def __init__(self, name='Skeleton'):
        self.name = name
        self.maxhp = 15
        self.hp = self.maxhp
        self.strength = 3
        self.agility = 3
        self.gold = randint(1, 4)


# Decides the enemy
def enemy_decider():
    global enemy
    num = randint(1, 2)
    if num == 1:
        enemy = Skeleton()
    elif num == 2:
        enemy = Zombie()
    print('A {} suddenly appears!'.format(enemy.name))


def fight():

    enemy_decider()
    print(enemy.name)

    while p1.hp >= 0 | enemy.hp >= 0:
        print('1) Attack')
        print('2) Run')
        option = input('>>> ')
        if option == '1':
            attack(p1, enemy)
            print('')
        elif option == '2':
            pass

    print('fight() ended')
    print(p1.__dict__)
    print(enemy.__dict__)


def attack(p1, enemy):
    damage = p1.strength + randint(-2, 2)
    if p1.hp > 0:
        enemy.hp -= damage
        print('You attack the {} for {} damage.'.format(enemy.name, damage))
    damage = enemy.strength + randint(-2, 2)
    if enemy.hp > 0:
        p1.hp -= damage
        print('The {} hit you for {} damage!'.format(enemy.name, damage))

    # Prints status of player and enemy
    if p1.hp > 0:
        print('Your hp: {}/{}'.format(p1.hp, p1.maxhp))
    elif p1.hp <= 0:
        print('Oh dear, you died.')
        main_menu()
    if enemy.hp > 0:
        print('{} hp: {}/{}'.format(enemy.name, enemy.hp, enemy.maxhp))
    elif enemy.hp <= 0:
        print('You killed the {}!'.format(enemy.name))
        p1.gold += enemy.gold
        menu(p1)


def store():
    pass

main_menu()