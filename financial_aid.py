student = input('Answer yes or no with no caps, are you a new student or current student?')
if student == 'yes':
    print('Proceed to next question')
else:
    print('Must be attending school or just starting to qualify')

gpa = float(input('What is your current gpa?'))
if gpa >= 2.0:
    print('Proceed to next question')
elif gpa >= 3.0:
    print('Proceed to next question')
elif gpa >= 4.0:
    print('Proceed to next question')
else:
    print('Must have a 2.0 or higher to qualify')

record = input('Answer yes or no with no caps, do you have any criminal records of drugs?')
if record == 'yes':
    print('Must have an clean record to qualify')
else:
    print('Proceed to next question')

hours = input('Answer yes or no with no caps, do you have a minimum of six credit hours of classes?')
if hours == 'yes':
    print('Proceed to next question')
else:
    print('You need a minimum of six credit hours to qualify')

money = float(input('What is your gross yearly income?'))
if money >= 50000:
    print('Sorry you do not qualify for financial aid')
else:
    print('You qualify for financial aid!')
