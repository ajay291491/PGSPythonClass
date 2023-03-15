year = int(input("Please provide a year"))
if year % 400 == 0 and year % 100 == 0:
    print("It is a leap year")
elif year % 100 == 0 and not year % 400 == 0:
    print('It is not a leap year')
elif year % 4 == 0 and year % 400:
    print('It is a leap year')
elif year % 4 == 0 and not year % 100 == 0:
    print('It is a leap year')
else:
    print('It is not a leap year')