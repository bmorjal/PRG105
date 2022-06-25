def main():
    file = input('Enter file name: ')
    try:
        secret = open('secret-code.txt', 'r')
        print('File ' + file + ' exists')
        print('secret phrase below')
        for line in secret:
            print(line)
        secret.close()
    except IOError:
        print('File does not exist')
    decode(line)


def decode(line1):
    code = ['0', '#', '@', '$', '%', '^', '&', '*', '(', ')',
            '_', '-', '=', '+', ';', ':', '"', '<', '>', '/',
            '`', '~', '4', '9', 'S', 'J', ' ', ',', '!', '?']

    standard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '!', '?']
    outfile = open("decode.txt", "w")
    code_final = ""
    for letter in line1:
        for item in range(0, len(code)):
            if letter == code[item]:
                code_final += (standard[item] + " ")
                outfile.write(standard[item])
    outfile.close()
    print(code_final)


main()
