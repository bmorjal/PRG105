def main():

    grade_file = open('grade.txt', 'w')

    user_data = int(input('How many students? '))
    for count in range(1, user_data + 1):
        name = input('Enter the name of the student: ')
        grade = input('Enter the grade of the student: ')
        grade_file.write("'" + name + "'" + ", " + "'" + grade + "'" + "\n")
    grade_file.close()


main()
