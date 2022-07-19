"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)
# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors


class Dwelling:
    def __init__(self, number_of_rooms, square_feet, floors):
        self.__number_of_rooms = number_of_rooms
        self.__square_feet = square_feet
        self.__floors = floors

# 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set__rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    def set__feet(self, square_feet):
        self.__square_feet = square_feet

    def set__floors(self, floors):
        self.__floors = floors

# 3) Add accessors for all of the data attributes
    def get__rooms(self):
        return self.__number_of_rooms

    def get__feet(self):
        return self.__square_feet

    def get__floors(self):
        return self.__floors

# 4) Create the class SingleFamilyHome as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes


class SingleFamilyHome(Dwelling):
    def __init__(self, number_of_rooms, square_feet, floors, yard_size, garage_type):
        super().__init__(number_of_rooms, square_feet, floors)
        self.__yard_size = yard_size
        self.__garage_type = garage_type
# 5) Create the mutator and accessor methods for the garage_type and yard_size attributes

    def set__garage(self, garage_type):
        self.__garage_type = garage_type

    def set__yard(self, yard_size):
        self.__yard_size = yard_size

    def get__garage(self):
        return self.__garage_type

    def get__yard(self):
        return self.__yard_size

# Demonstrate the SingleFamilyHome class, no need to import because you are in the same file
# 6) Create a main function.
# 7) In main, create an object from the Single_family_home class with the following information:
#            6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres


def main():
    house1 = SingleFamilyHome('6 rooms', '1200 square feet', '1 floor', '.25 acres', 'single car garage')
# 8) Display the data using the accessor methods
    print(house1.get__rooms())
    print(house1.get__feet())
    print(house1.get__floors())
    print(house1.get__garage())
    print(house1.get__yard())
# 9) Call the main function


main()


# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)
# 1) Type in the mammal class from program 11-9, lines 1 - 22


class Mammal:
    def __init__(self, birth, blood, hair):
        self.__birth_type = birth
        self.__blood = blood
        self.__hair = hair

    def set__birth_type(self, birth):
        self.__birth_type = birth

    def set__blood(self, blood):
        self.__blood = blood

    def set__hair(self, hair):
        self.__hair = hair

    def get__birth_type(self):
        return self.__birth_type

    def get__blood(self):
        return self.__blood

    def get__hair(self):
        return self.__hair
# 2) Create a Mouse class as a sub class of the mammal class following the Dog example


class Mouse(Mammal):
    def __init__(self, birth, blood, hair):

# 3) Create an Sheep class as a sub class of the mammal class following the Cat Example

# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
#    because there is already a main on this page) use the Mouse and Sheep class that you created
