def oneline(s):
    return ' '.join(s.strip().split())




class Player:

    def __init__(self, typ, subtype, element):
        self.typ = typ
        self.subtype = subtype
        self.element = element

    def describe(self):
        return oneline(f'''You are of the class {self.type}, of the subclass
        {self.subtype}, and specialize in the element {self.element}
        ''')

    def raw_data(self):
        return '{} {} {}'.format(self.type, self.subtype, self.element)

    @classmethod
    def create_from_input(cls):
        typeOptions = ['Warrior', 'warrior', 'Wizard', 'wizard', 'Archer', 'archer']

        print('Create your player')
        while True:
            typ = input('Enter a type:  ')
            if typ in typeOptions:
                break
            else:
                print('Enter "warrior", "wizard", or "archer"')

        player = cls(type=type, subtype=subtype, element=element)
        print(player.describe())
        return player

class Monster:
    pass

class Subtype(Player):
    # # # subtypeOptions = ['Pirate', 'pirate', 'Robot', 'robot', 'Alien', 'alien']
    # # # def __init__():
    # # #     super().__init__():
    # # # while True:
    # # #         subtype = input('Enter a subtype:  ')
    # # #         if subtype in subtypeOptions:
    # # #             break
    # # #         else:
    # # #             print('Enter "pirate", "robot", or "alien"')
    pass








class Stats():
    def __init__(self, hp=50, damage=10, strength=0, mana=0):
        self.hp = hp
        self.damage = damage
        self.strength=strength
        self.mana=mana

    def __str__(self):
        return oneline(f'''\
            HP: {self.hp}
            Damage: {self.damage}
            Strength: {self.strength}
            Mana: {self.mana}\n''')



#Player.create_from_input()
