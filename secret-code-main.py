def main():

    code = ['0', '#', '@', '$', '%', '^', '&', '*', '(', ')',
            '_', '-', '=', '+', ';', ':', '"', '<', '>', '/',
            '`', '~', '4', '9', 'S', 'J', '', ',', '!', '?']

    standard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z', '', '.', ',', '!', '?']

    phrase = input('Please enter phrase to translate into the secret code: ')

    outfile = open("secret-code.txt", "w")
    code_final = ""
    for letter in phrase:
        for item in range(0, len(standard)):
            if letter.upper() == standard[item]:
                code_final += (code[item] + " ")
                outfile.write(letter + '\n')
                outfile.write(code[item] + '\n')
    outfile.close()
    print(code_final)


main()
