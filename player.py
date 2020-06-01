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
        typeOptions = ['Warrior', 'warrior', 'Wizard', 'wizard', 'Archer', 'archer'] #easier way to make it case insensitive?
        subtypeOptions = ['Pirate', 'pirate', 'Robot', 'robot', 'Alien', 'alien']

        print('Create your player')
        while True:
            typ = input('Enter a type:  ')
            if typ in typeOptions:
                break
            else:
                print('Enter "warrior", "wizard", or "archer"')

        while True:
            subtype = input('Enter a subtype:  ')
            if subtype in subtypeOptions:
                break
            else:
                print('Enter "pirate", "robot", or "alien"')

        while True:
            element = input('Enter an element:  ')
            if element in elementOptions:
                break
            else:
                print('Enter "fire", "water", or "darkness"')

        player = cls(type=type, subtype=subtype, element=element)
        print(player.describe())
        return player

class Monster:
    pass

Player.create_from_input()
