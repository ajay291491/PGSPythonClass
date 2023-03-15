"""
Team : Green (Dhruv Praveen, Nidhi Math, Ishi Rakesh, Nandanram Gopireddy)

Assessment & Comments

. Good
- Working program, but the calculations are not right
- Comments are clear

. Areas to Improve
- Calculation are not right and did not given expected result
- Could try more

 * Marks *
Working program : 3/5
Code Quality    : 2/3
Comments used   : 2/2
Total           : 7/10
"""

year = int(input("enter year"))
if year%4==0 and year%400==0 or year%100!=0 :
    print("Its a Leap Year")
else :
    print("Its not a leap year")