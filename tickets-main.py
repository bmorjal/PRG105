print('Buying tickets')

print('1. Student $5.00')
print('2. Veteran $7.00')
print('3. Sponsor $2.00')
print('4. Retiree $6.00')
print('5. General $10.00')

category = float(input('Please enter the number of the category you fit for purchasing:'))
ticket = float(input('How many tickets would you like to buy?'))
print('')
if category == 1:
    amount = 5.00 * ticket
    print('Before discount', amount)
    if 4 <= ticket <= 8:
        disc = float(amount * .10)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif 9 <= ticket <= 15:
        disc = float(amount * .15)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif ticket > 15:
        disc = float(amount * 0.20)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    else:
        print('none')
elif category == 2:
    amount = 7.00 * ticket
    print('Before discount', amount)
    if 4 <= ticket <= 8:
        disc = float(amount * .10)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif 9 <= ticket <= 15:
        disc = float(amount * .15)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif ticket > 15:
        disc = float(amount * 0.20)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    else:
        print('none')
elif category == 3:
    amount = 2.00 * ticket
    print('Before discount', amount)
    if 4 <= ticket <= 8:
        disc = float(amount * .10)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif 9 <= ticket <= 15:
        disc = float(amount * .15)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif ticket > 15:
        disc = float(amount * 0.20)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    else:
        print('none')
elif category == 4:
    amount = 6.00 * ticket
    print('Before discount', amount)
    if 4 <= ticket <= 8:
        disc = float(amount * .10)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif 9 <= ticket <= 15:
        disc = float(amount * .15)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif ticket > 15:
        disc = float(amount * 0.20)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    else:
        print('none')
elif category == 5:
    amount = float(10.00 * ticket)
    print('Before discount', amount)
    if 4 <= ticket <= 8:
        disc = float(amount * .10)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif 9 <= ticket <= 15:
        disc = float(amount * .15)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    elif ticket > 15:
        disc = float(amount * 0.20)
        final = float(amount - disc)
        per = float(final / ticket)
        print('After discount', final)
        print('Your price per ticket', per)
    else:
        print('none')
else:
    print('Not valid')
