PI = 3.14


def main():
    menu = 0
    while menu < 5:
        print('1. rectangle\n 2. triangle\n 3. square\n 4. circle\n 5. quit')
        menu = int(input('pick a menu option: '))
        if menu == 1:
            print('You picked rectangle')
            rectangle()
        elif menu == 2:
            print('You picked triangle')
            triangle()
        elif menu == 3:
            print('You picked square')
            square()
        elif menu == 4:
            print('You picked circle')
            circle()
        else:
            print('Goodbye')


def rectangle():
    width = float(input('Enter width here: '))
    length = float(input('Enter length here: '))
    area = width * length
    print(area)


def triangle():
    base = float(input('Enter base here: '))
    height = float(input('Enter height here: '))
    area = (base * height) / 2
    print(area)


def square():
    side = float(input('Length of a side: '))
    area = side * side
    print(area)


def circle():
    radius = float(input('Radius: '))
    area = PI * (radius * radius)
    print(area)


main()
