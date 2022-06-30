def main():
    user_input = input('Input a phrase here: ')
    user_input = user_input.upper()
    list1 = user_input.split()
    for word in list1:
        print(word[0])


main()
