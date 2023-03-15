"""
Team : Purple (Sri Agastya Jasti, Gutha Vedanth, Guraja Meghan)

Assessment & Comments
. Good
- Working program and meet the purpose of logic
- Comments for user input is very clear
- print statements are very clear

. Areas to Improve
- Avoid capital letters in variable names

 * Marks *
Working program : 5/5
Code Quality    : 2/3
Comments used   : 2/2
Total           : 9/10
"""

English=int(input("enter marks for english"))  # => english_mark=int(input("enter marks for english"))
lang2=int(input("enter marks for 2nd lang"))
science=int(input("enter marks for science"))
maths=int(input("enter marks for maths"))
social=int(input("enter marks for social"))
total=English+lang2+maths+science+social
average =total/5
print("your average is:{}".format(average))
if average <=80:
    print("grade is A")
elif average <=60:
    print("grade is b")
elif average <=40:
    print("grade is c")
else:
    print("you failed")