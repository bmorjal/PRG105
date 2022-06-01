print('Sales calculator')
print('')
total = 0
for day in "Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun":
    day_sale = float(input('What was the total sale for ' + day + ":"))
    total += day_sale
daily = (total / 7)
final = '${:,.2f}'.format(total)
average = '${:,.2f}'.format(daily)
print('Total amount of sale for the week, ' + final)
print('The average amount of sales per day was, ' + average)
