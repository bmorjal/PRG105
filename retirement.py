age = int(input('How old are you? '))
retire = int(input('What age do you wish to retire? '))
income = int(input('What is your yearly income, format to whole number? '))
savings_percent = float(input('What percent of your income do you save, format to decimal? '))
total_savings = int(input('How much do you currently have in savings, format to whole number? '))
contribution = income * savings_percent
total_savings = (total_savings * 1.06 + contribution)
year = retire - age

for num in range(1, year):
    print('Year')
    print(num)
    for income_2 in range(0, 1):
        print('Income')
        print(('${:,.0f}'.format(income)))
        income *= 1.03
        for contribution_2 in range(0, 1):
            print('Contribution')
            print('${:,.0f}'.format(contribution))
            contribution = income * savings_percent
            for total_saving_2 in range(0, 1):
                print('Total Savings')
                print('${:,.0f}'.format(total_savings))
                print('')
                total_savings = (total_savings * 1.06 + contribution)
