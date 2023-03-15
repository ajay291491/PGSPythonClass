#Question1
'''
Eng = float(input("What are your marks in English?"))
Lang_2 = float(input("What are your marks in Lang 2?"))
Maths = float(input("What are your marks in Maths?"))
Science= float(input("What are your marks in Science?"))
SST= float(input("What are your marks in SST?"))

total_marks =Eng + Lang_2 + Maths + Science + SST
average = total_marks / 5
if average >= 80:
    print("Your grade is A")
elif average >= 60:
    print("Your grade is B")
elif average >= 40:
    print("Your grade is C")
else:
    print("Sorry,you've failed")
print(f"Your total marks are {total_marks}")
'''
#Question 2

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


