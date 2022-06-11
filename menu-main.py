

def main():
    print('Select one of the menu options below to find out more')
    print('A. Rodeo Burger')
    print('B. Meat Lover Burger')
    print('C. Pizza Burger')
    print('D. Spanish Burger')
    print('E. Not So Burger')
    choice = input('Enter the letter of your choice lowercase: ')
    if choice == 'a':
        print('Rodeo Burger')
        print('6 ounce burger, cheddar cheese,  fried onions, bbq sauce')

    elif choice == 'b':
        print('Meat Lover Burger')
        print('2 6 ounce burger, honey smoked bacon, pulled pork, bbq sauce')

    elif choice == 'c':
        print('Pizza Burger')
        print('6 ounce burger, peperoni, mozzarella, marinara sauce')

    elif choice == 'd':
        print('Spanish Burger')
        print('6 ounce burger, pico de gallo, guacamole, spicy mayo sauce')

    elif choice == 'e':
        print('Not So Burger')
        print('6 ounce impossible burger, lettuce, pickles, tomatoes, portabella mushroom, avocado sauce')

    else:
        print('Not an option')


main()
