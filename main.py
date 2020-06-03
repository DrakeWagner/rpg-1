import sys
import os

for i in range(0,5):
    print(' ')
print('===================================================')
print('=========== Welcome to rpg_1_test =================')
print('===================================================')


def menu():
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
        menu()

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

def start():
    os.system('cls')
    p1 = Player_Class()
    p1.pick_class()
    print(p1)


    
    




menu()