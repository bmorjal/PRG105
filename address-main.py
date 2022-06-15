print('Contact information storage')
address_data = open('address.txt', 'w')
user_data = int(input('How many people do you want to add to file? '))
for count in range(1, user_data + 1):
    name = input('What is the name of the person? ')
    number = input('What is their phone number? ')
    email = input('What is their email address? ')
    address_data.write(name + ', ' + number + ', ' + email + '\n')
address_data.close()
