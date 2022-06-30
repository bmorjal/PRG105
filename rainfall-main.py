def main():
    total = 0.0
    count = 0
    file1 = open('rainfall.txt', 'r')
    for line in file1:
        line = line.rstrip("\n")
        list1 = line.split()
        month = list1[0]
        amt = list1[1].split('.')

        if amt[0].isdigit() and amt[1].isdigit():
            amount = float(amt[0] + "." + amt[1])
            total += float(amount)
            count += 1
        else:
            print(month + " is not valid because")
            print(str(list1[1]) + " is not a number")
    print("The total rainfall for " + str(count) + " month is " + format(total, ',.2f'))
    print("The average rainfall was " + format((total/count), ',.2f'))

    file1.close()


main()
