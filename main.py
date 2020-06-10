import sys
import os
from random import randint

for i in range(0,5):
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
        def __init__(self, myclass=None, hp=0, strength=0, agility=0, gold=0):
            self.myclass=myclass
            self.hp=hp
            self.strength=strength
            self.agility=agility
            self.gold=gold

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
                self.maxhp=25
                self.hp=25
                self.strength=3
                self.agility=1
            if self.myclass == 'archer':
                self.hp=15
                self.strength=5
                self.agility=3
            if self.myclass == 'wizard':
                self.hp=10
                self.strength=6
                self.agility=2

def start():
    os.system('cls')
    p1 = Player_Class()
    p1.pick_class()
    print(p1)
    menu(p1)


# Main loop of the game
def menu(p1):

    global Player_Class

    print('================')
    print('Gold: %i' % (p1.gold))
    print('HP: %i' % (p1.hp))
    print(' ')
    print('1) Fight')
    print('2) Store')
    print('3) Player Info')
    print('4) Main Menu')
    option = int(input('>> '))
    if option == 1:
        enemy_decider()
    elif option == 2:
        store()
    elif option == 3:
        print(p1.__dict__)
    elif option == 4:
        main_menu()

class Skeleton:
    def __init__(self, name):
        self.name = name
        self.maxhp = 15
        self.hp = self.maxhp
        self.attack = 3
        self.agility = 3
test_skeleton = Skeleton('test_skeleton')

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhp = 20
        self.hp = self.maxhp
        self.attack = 5
        self.agility = 1
test_zombie = Zombie('test_zombie')


enemy=0
def enemy_decider():
    global enemy
    num = randint(1,2)
    if num == '1':
        enemy=test_skeleton
    elif num =='2':
        enemy=test_zombie
    fight()


def fight():
    print('A {} suddenly appears!'.format(enemy.name))
    print('1) Attack')
    print('2) Run')
    option = input('')
    if option =='1':
        attack()
    if option =='2':
        run()

def attack(p1):
    damage = p1.strength + randint(-2, 2)
    enemy.hp -= damage
    print('You attack the {} for {} damage.'.format(enemy.name, damage))
    damage = enemy.strength + randint(-2, 2)
    p1.hp -= damage
    print('The {} hit you for {} damage!'.format(enemy.name, damage))

def store():
    pass







    
    




main_menu()