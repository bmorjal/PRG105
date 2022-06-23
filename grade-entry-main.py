def main():

    line = []
    student_grades = []
    count = int(input("How many students? "))
    for student in range(0, count):
        student_name = input("Enter the students name " + str(student + 1) + ": ")
        grade = input("Enter the final letter grade of the student: ")
        line.append(student_name)
        line.append(grade)
        student_grades.append(line)
        line = []
    print(student_grades)

    outfile = open("grade.txt", "w")
    for line in student_grades:
        lineout = "'" + line[0] + "', '" + line[1] + "'\n"
        outfile.writelines(lineout)
    outfile.close()


main()
