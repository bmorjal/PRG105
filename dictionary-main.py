def main():
    number_of_days = 7
    days_and_steps = {}
    for i in range(number_of_days):
        day = input("Enter the day of the week: ")
        steps = int(input("Enter the amount of steps taken: "))
        days_and_steps[day] = steps

    print('You walked a total of', sum(days_and_steps.values()), 'steps during the week.')
    res = 0
    for val in days_and_steps.values():
        res += val

    av = res / 7
    print('The average was', format(av, '.0f'))

    max_value = max(days_and_steps.values())
    max_day = max(days_and_steps.keys())
    print('The maximum steps you took were:', max_value, 'on', max_day)

    min_value = min(days_and_steps.values())
    min_day = min(days_and_steps.keys())
    print('The minimum steps you took were:', min_value, 'on', min_day)


main()
