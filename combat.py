from random import randint

def Player_Attack(player, enemy):
    damage = player.strength + randint(-2, 2)
    enemy.hp -= damage
    print('You attack the {} for {} damage.'.format(enemy.name, damage))

def Enemy_Attack(player, enemy):
    damage = enemy.strength + randint(-2, 2)
    player.hp -= damage
    print('The {} hit you for {} damage!'.format(enemy.name, damage))
    

def combat_commands(player, enemy):
    pass
    while enemy.hp and player.hp > 0:
        print('Press f to fight, h to heal, s to see status, or r to run')
        command=input('>> ')
        if command=='f':
            Player_Attack(player, enemy)
            Enemy_Attack(player, enemy)
        elif command=='h':
            pass
        elif command=='s':
            print(player.__dict__)
        
def run(player, enemy):
    running_number = randint(1, 3)
    if running_number > 1:
        print('You have run away successfully!')
    else:
        print('You failed to get away!')
        Enemy_Attack(player, enemy)