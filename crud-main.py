import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open("customer_data.dat", "rb")
        customers = pickle.load(input_file)

    except (FileNotFoundError, IOError):
        print("file not found, please add a customer then quit to create file")
        customers = {}

    choice = 0

    while choice != QUIT:
        choice = menu()

        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)


def menu():
    print()
    print("Customer email lookup")
    print("---------------------")
    print("1. Look up customer")
    print("2. Add new customer")
    print("3. Change an email address")
    print("4. Delete customer")
    print("5. Quit the program\n")

    choice = int(input("Enter number of your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input("Enter a valid choice: "))
    return choice


def look_up(customers):
    name = input("Enter a customer name: ")
    print(customers.get(name, 'Not Found'))


def add(customers):
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    if name not in customers:
        customers[name] = email
    else:
        print("That entry already exists.")


def change(customers):
    name = input("Enter customer name: ")
    if name in customers:
        email = input("Enter the new email: ")
        customers[name] = email
    else:
        print("That customer is not found.")


def delete(customers):
    name = input("Enter customer name: ")
    if name in customers:
        del customers[name]
    else:
        print("That customer is not found.")


def save(customers):
    print("The data file has been updated with your changes. ")
    save_file = open("customer_data.dat", "wb")
    pickle.dump(customers, save_file)
    save_file.close()


main()
