"""
Team : Yellow (Basani Srinivasa Aditya, Utkarsha Pande, Satnam Arvind Dhondphale)

Assessment & Comments
. Good
- Working program
- Comments are very clear
- Calculation are right and given expected result

. Areas to Improve
None

 * Marks *
Working program : 5/5
Code Quality    : 3/3
Comments used   : 2/2
Total           : 10/10
"""

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