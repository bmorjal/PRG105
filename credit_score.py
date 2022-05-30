print('Credit score program')
print('')

credit = float(input('What is your credit score?'))
if credit <= 629:
    print('With a score of', credit)
    print('You have bad credit score')
elif credit <= 689:
    print('With a score of', credit)
    print('You have fair credit score')
elif credit <= 719:
    print('With a score of', credit)
    print('You have good credit score')
elif credit <= 850:
    print('With a score of', credit)
    print('You have excellent credit score')
