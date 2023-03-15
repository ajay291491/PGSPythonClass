"""
Team : Red (Dugandla Enosh Preetham Reddy, Badveli Meghana Reddy, Siddhanth K.P)

Assessment & Comments

. Good
- Working program, but the calculations are not right
- Comments are very clear

. Areas to Improve
- Calculation are not right and did not given expected result
- Could try more

 * Marks *
Working program : 3/5
Code Quality    : 2/3
Comments used   : 2/2
Total           : 7/10
"""


year=(int)(input("enter the year"))
if year%4==0 and year%400==0 and year%100==25:
    print(" yes leap year")
else:
    print(" not a leap year")