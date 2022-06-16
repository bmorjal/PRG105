def main():
    error = open('sales_error.txt', 'r')
    counter = 0
    try:
        for line in error:
            print(float(line))
            counter += 1
    except ValueError:
        print('line', counter, ' with the value of', line, ' was invalid')

    import os
    
    fn = input('Enter file name to read: ')
    if os.path.isfile(fn):
        print('File exists')
    else:
        print('File does not exist')

    error.close()


main()
