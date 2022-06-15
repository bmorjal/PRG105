def main():
    my_file = 'numbers.txt'
    number_file = open(my_file, 'r')
    counter = 0
    sum1 = 0
    average = 0
    for line in number_file:
        print(line)
        counter += 1
    print('Number of entities: ' + str(counter))

    with open(my_file) as number_file:
        for n in number_file:
            n = n.strip()
            sum1 = sum1 + float(n)
            average = sum1 / counter
    print('Sum equals:', format(sum1, ',.2f'))
    print('Average:', format(average, ',.2f'))

    number_file.close()


main()
