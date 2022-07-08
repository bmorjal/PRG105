def main():
    print('This quiz will be going through spanish numbers')
    print('You will be giving the spanish number and you must input the english equivalent')
    questions = {'Translate Uno': 'one', 'Translate Dos': 'two', 'Translate Tres': 'three', 'Translate cuatro': 'four',
                 'Translate Cinco': 'five', 'Translate Seis': 'six', 'Translate Siete': 'seven',
                 'Translate Ocho': 'eight', 'Translate Nueve': 'nine', 'Translate Diez': 'ten'}
    score = 0
    for i in questions:
        print(i)
        ans = input("Enter answer word all lowercase: ")
        if ans == questions[i]:
            print('Correct')
            score = score + 1
        else:
            print('Incorrect, the answer was', questions[i])
            score = score - 1
    if score == 10:
        print('You got a A')
    elif score == 9:
        print('You got a A')
    elif score == 8:
        print('You got a B')
    elif score == 7:
        print('You got a C')
    elif score == 6:
        print('You got a D')
    else:
        print('You got a F')


main()
