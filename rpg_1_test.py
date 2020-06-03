from random import randint
import time

if __name__ == "__main__":
    pass

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
    # Sets the default stats
    # hp = health
    # strength = power
    # agility = chance of dodging an attack
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

    def is_alive(self):
        return self.hp>0

    def pick_subclass(self):
        mysubclassOptions = ['pirate', 'alien', 'robot']
        pass

    def raw_data(self):
        return '{} {} {}'.format(self.type, self.subtype, self.element)

# class Warrior(Player_Class):
#     def __init__(self):
#         super().__init__(hp=25, strength=3, agility=1)
    
#         self.hp=25
#         self.strength=3
#         self.agility=1


class Archer(Player_Class):
    pass

class Wizard(Player_Class):
    pass
    
    

# Combat mechanism
def attack(player, enemy):
        print('A {} appears!'.format(enemy.name))
        while enemy.is_alive() and player.is_alive() == True:
            
            # Player's Attack
            damage = player.strength + randint(-2, 2)
            enemy.hp -= damage
            print('You attack the enemy for {} hp'.format(damage))
            
            #Enemy's attack
            enemy_damage = enemy.strength + randint(-2, 2)
            if enemy.is_alive() == True:
                player.hp -= enemy_damage
                print('The {} attacks your for {} hp.'.format(enemy.name, enemy_damage))
            print('Your health is now {}.'.format(player.hp))
            if enemy.is_alive() == True:
                print("The {}'s hp is {}.".format(enemy.name, enemy.hp))
            elif enemy.is_alive() == False:
                print('The {} is staggering...'.format(enemy.name))
            print(' ')
            input('Press enter to attack again...')
            continue
        if not enemy.is_alive():
            # Enemy death
            print('You killed the {}!'.format(enemy.name))
            print('The {} dropped {} gold.'.format(enemy.name, enemy.carried_gold))
            player.gold += enemy.carried_gold
            print('You now have ' + str(player.gold) + ' gold', sep='')
        elif not player.is_alive():
            # Player death
            print('You have died!')

        








# def status(player):
#     # Tells the player their current stat attributes
#     print('Hp: {}/{}'.format(player.hp, player.maxhp)
    

class Monster:
    #Defines the different enemies
    def __init__(self, name, hp, strength, agility, carried_gold):
        self.name=name
        self.hp=hp
        self.strength=strength
        self.agility=agility
        self.carried_gold = carried_gold

    def is_alive(self):
        return self.hp>0

class Skeleton(Monster):
    def __init__(self):
        super().__init__(name='Skeleton',
                        hp=randint(10, 13), 
                        strength=2, 
                        agility=4,
                        carried_gold=randint(3, 5))

class Zombie(Monster):
    def __init__(self):
        super().__init__(name='Zombie',
                         hp=randint(13, 17),
                         strength=4,
                         agility=1,
                         carried_gold=randint(5, 7))



# ====================== #
test_player = Player_Class()
test_player.pick_class()


test_skeleton = Skeleton()




# combat_commands(test_player, test_skeleton)
