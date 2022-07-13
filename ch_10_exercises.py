"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

import random
# TODO 10.2 modify Coin class to Dice
print("=" * 10, "Section 10.2 Coin class to Dice class", "=" * 10)

""""
class Dice:  # note class names are capitalized
    def __init__(self, sides):
        # TODO change side_up to '1'
        self.__sides = sides
        self.__side_up = 1

        # TODO change toss() to roll()
    def roll(sides):
        # TODO get a random value and set side_up for the 6 sides of the dice
        self.sides = sides
            
    def get_sides(self):
        return self.sides
    

def main():
    # TODO change my_coin to my_dice, my_dice_two and the appropriate class name throughout main
    my_dice = Dice()
    my_dice_two = Dice()
    print('This side is up, ', my_dice.get_sides())
    print('This side is up, ', my_dice_two.get_sides())
    
    print('I am tossing the coins...')
    my_dice.roll()
    my_dice_two.roll()
    print('This side is up, ', my_dice.get_sides())
    print('This side is up, ', my_dice_two.get_sides())


main()
"""

for i in range(1):
    player_value = random.randint(1, 6)
    print("Player rolled a", player_value)
