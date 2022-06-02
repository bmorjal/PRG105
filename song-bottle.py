def sing(n):
    if n == 1:
        objects = 'bottle'
        objects_minus_one = 'bottles'
    elif n == 2:
        objects = 'bottles'
        objects_minus_one = 'bottle'
    else:
        objects = 'bottles'
        objects_minus_one = 'bottles'

    if n > 0:
        print(str(n) + " " + objects + " of beer on the wall, ")
        print(str(n) + " " + objects + " of beer.")
        print("Take one down, pass it around, ")
        print(str(n-1) + " " + objects_minus_one + " of beer on the wall.")
        print(" ")
    else:
        print("No more bottles of beer on the wall!")


bottles = 99


while bottles >= 0:
    sing(bottles)
    bottles -= 1
