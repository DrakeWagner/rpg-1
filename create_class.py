class Player:
    def __init__(self, type, subtype, element):
        self.type = type
        self.subtype = subtype
        self.element = element

    def describe_player(self):
        print('You are of the class ' + self.type + \
            ', of the subclass '+ self.subtype + \
            ', and specialize in the element ' + self.element
        )
#inputType, inputSubtype, inputElement
yes = ['y', 'Y', 'Yes', 'yes', 'Yeah', 'yeah', 'yep', 'Yep', 'sure', 'Sure', 'yeet!']
no = ['n', 'N', 'No', 'no', 'Nah', 'nah', 'Nope', 'nope', 'noo', 'Noo']

def player_class():
    typeOptions = ['Warrior', 'warrior', 'Wizard', 'wizard', 'Archer', 'archer'] #easier way to make it case insensitive?
    subtypeOptions = ['Pirate', 'pirate', 'Robot', 'robot', 'Alien', 'alien']

    #Type
    print('Will you be a warrior, wizard, or archer? Enter one:  ')
    h = 0
    while h == 0:
        typeInput = input('**type** ')
        if typeInput in typeOptions:
            print('You have chosen ', typeInput, '. Is this correct? <Y or N>', sep='')
            typeConfirmation = input('')
            if typeConfirmation in yes:
                print('Confirmed')
                h += 1
            elif typeConfirmation in no:
                print('Okay, please repick your type')
            else:
                print("I didn't understand that.")
        else:
            print("I don't understand. Please try again.")
    

    ### Subtype now
    print("So you're a ", typeInput, ", eh?", sep="")
    print('Will your subtype be pirate, robot, or alien?')
    h=0
    while h == 0:
        subtypeInput = input('**subtype** ')
        if subtypeInput in subtypeOptions:
            print('You have chosen ', subtypeInput, '. Is this correct? <Y or N>', sep='')
            subtypeConfirmation = input()
            if subtypeConfirmation in yes:
                print('Confirmed')
                h += 1
            elif subtypeConfirmation in no:
                print('Okay, please repick your subtype')
            else:
                print('I didn\'t understand that.')
        else:
            print('I don\'t understand. Please try again.')

 
    ### Element now
    print('Interesting choice. Lastly, you will choose an element to specialize in.')
    print('Will you focus your mana on Fire, Water, or Air?')
    airElement = ['air', 'Air']
    fireElement = ['fire', 'Fire']
    waterElement = ['water', 'Water']
    h=0
    while h == 0:
        elementInput = input('**element** ')
        if elementInput in airElement:
            print('You have chosen to focus your powers on wind and Air. Is this correct? <Y or N>', sep='')
            subtypeConfirmation = input()
            if subtypeConfirmation in yes:
                print('Confirmed')
                h += 1
            elif subtypeConfirmation in no:
                print('Okay, please repick your element')
            else:
                print('I didn\'t understand that.')
        if elementInput in fireElement:
            print('You have chosen to focus your powers on Fire. Is this correct? <Y or N>', sep='')
            subtypeConfirmation = input()
            if subtypeConfirmation in yes:
                print('Confirmed')
                h += 1
            elif subtypeConfirmation in no:
                print('Okay, please repick your element')
            else:
                print('I didn\'t understand that.')
        if elementInput in waterElement:
            print('You have chosen to focus on Water. Is this correct? <Y or N>', sep='')
            subtypeConfirmation = input()
            if subtypeConfirmation in yes:
                print('Confirmed')
                h += 1
            elif subtypeConfirmation in no:
                print('Okay, please repick your element')
            else:
                print('I didn\'t understand that.')
        
#Make typeInput, subtypeInput, and elementInput correlate with the init of class Player


### Attempt to make the confirmations a function to clear the lines up more
# def checkList(element, list):
#     global h
#     if element in list:
#         print('You have chosen to focus your powers on ', element, '. IS this correct? <Y or N>', sep='')
#         doublecheck = input()
#         if doublecheck in yes:
#             print('Confirmed')
#             h += 1
     



# Player1 = Player('wizard', 'mage', 'fire')
# Player1.describe_player()


# a = Player(player_class())
# a
# a.describe_player()

a = player_class()
print(a)