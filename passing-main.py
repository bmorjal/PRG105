

def main():
    number = int(input('Enter a whole number between 20 and 100: '))
    validate(number)
    divisible(number)


def validate(num):
    while True:
        if 20 <= num <= 100:
            print('yes')
            break
        else:
            print('Not a valid value')
            return main()


def divisible(num):
    number_2 = num % 2
    number_3 = num % 3
    number_4 = num % 5
    if number_2 == 0:
        print(num, 'is divisible by two')
    else:
        print(num, 'is not divisible by two')

    if number_3 == 0:
        print(num, 'is divisible by three')
    else:
        print(num, 'is not divisible by three')

    if number_4 == 0:
        print(num, 'is divisible by five')
    else:
        print(num, 'is not divisible by five')


main()
