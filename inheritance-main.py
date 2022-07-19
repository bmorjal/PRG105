class Office_Funiture(object):
    def __init__(self, material, length, width, height, price):
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):
        line_item = 'Item is made of ' + self.__material + ' with length of ' + self.__length + ' height of ' + self.__height + ' width of ' + self.__width + ' with a price of ' + self.__price
        return line_item


class Desk(Office_Funiture):
    def __init__(self, material, length, width, height, price, location_of_drawers, number_of_drawers):
        super().__init__(material, length, width, height, price)
        self.__location = location_of_drawers
        self.__number = number_of_drawers

    def set_location(self, location_of_drawers):
        self.__location = location_of_drawers

    def set_number(self, number_of_drawers):
        self.__number = number_of_drawers

    def get_location(self):
        return self.__location

    def get_number(self):
        return self.__number

    def __str__(self):
        printline = "Desk is made of " + self.get_material() + ' with a length of ' + self.get_length() + ' height of ' + self.get_height() +\
            ' width of ' + self.get_width() + ' the price is ' + self.get_price() + ' the drawers are located on the ' + self.__location +\
            ' it has ' + self.__number + ' of drawers.'
        return printline


def main():
    desk1 = Office_Funiture('Wood', '6ft', '4ft', '3ft', '$400')
    print(desk1)

    print()

    desk2 = Desk('Metal', '8ft', '4ft', '4ft', '$1000', 'left side', '3')
    print(desk2)


main()
