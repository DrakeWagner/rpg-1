import random
def shop_intro_line():
    Lines = ['1A shopkeeper is standing at the counter, eating some mashed potatoes.',
             '2A shopkeeper is standing at the counter, eating some mashed potatoes.',
             '3A shopkeeper is standing at the counter, eating some mashed potatoes.',
             '4A shopkeeper is standing at the counter, eating some mashed potatoes.']
    randline = random.choice(Lines)
    print(randline)


shop_intro_line()

print(random.__file__)