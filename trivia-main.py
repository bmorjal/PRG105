import question


def main():
    q1 = question.Question("What temperature does water boil at?", "A. 100C", "B. 50C",
                           "C. 80C", "D. 120C", "A")
    q2 = question.Question("When was the first world war fought?", "A. 1920", "B. 1845",
                           "C. 1914", "D. 1980", "C")
    q3 = question.Question("How many bones in the human body?", "A. 200", "B. 130",
                           "C. 206", "D. 210", "C")
    q4 = question.Question("Who painted the mona lisa?", "A. Leonardo", "B. Julius",
                           "C. Abraham", "D. Washington", "A")
    q5 = question.Question("What comics was the movie suicide squad based on?", "A. Avengers", "B. Marvel",
                           "C. Scary Stories", "D. DC", "D")
    q6 = question.Question("What is the largest planet in the solar system?", "A. Saturn", "B. Jupiter",
                           "C. Uranus", "D. Pluto", "B")
    q7 = question.Question("Who is the lead actress of Hunger Games?", "A. Jennifer Lawrence", "B. Dwayne Johnson",
                           "C. Kevin Hart", "D. Jennifer Garner", "A")
    q8 = question.Question("Which planet is closet to the sun?", "A. Earth", "B. Saturn",
                           "C. Pluto", "D. Mercury", "D")
    q9 = question.Question("Bill gates is the founder of what?", "A. Apple", "B. Microsoft",
                           "C. Samsung", "D. Msi", "B")
    q10 = question.Question("What vitamin is in citrus fruit?", "A. C", "B. D",
                            "C. A", "D. F", "A")

    player1 = 0
    player2 = 0

    set_1 = [q1, q3, q5, q7, q9]

    set_2 = [q2, q4, q6, q8, q10]

    print("Player 1: ")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("Correct")
            player1 += 1
        else:
            print("Wrong")

    print("Player 1 earned: " + str(player1) + " points.")
    print("\n")
    print("Player 2: ")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("Correct")
            player2 += 1
        else:
            print("Wrong")

    print("Player 2 earned: " + str(player2) + " points.")

    if player1 == player2:
        print("It's a tie")
    elif player1 > player2:
        print("Player 1 won!")
    elif player1 < player2:
        print("Player 2 won!")


main()
