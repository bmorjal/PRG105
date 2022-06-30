def main():
    values = open("accounts.txt", "r")
    overdue = open("over90.txt", "r")
    for line in values:
        line = line.rstrip("\n")
        list1 = line.split(",")
        number1 = list1[0]

        for line1 in overdue:
            line1 = line1.rstrip("\n")
            list2 = line1.split(",")
            print(list2)
            number2 = list2[0]

            if number2 == number1:
                print(line)
            else:
                print('null')


main()
