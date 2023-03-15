"""
Assessment & Comments
. Good
- Overall program logic is good, but minor syntax issues caused the program not running

. Areas to Improve
- print statement can be made more clear
- Avoid capital letters in variable names
- print statement used variables names in lower case where it was declared with first letter capital above

 * Marks *
Working program : 3/5
Code Quality    : 1/3
Comments used   : 2/2
Total           : 6/10
"""

english=(int)(input("Enter your english marks"))
lang2=(int)(input("Enter your lang2 marks"))
maths=(int)(input("Enter your maths marks"))
science=(int)(input("Enter your science marks"))
social=(int)(input("Enter your social marks"))
Totalmarks=(english+lang2+maths+science+social)   # => variable declared with capital letter in beginning
Avgmarks=(Totalmarks/5)                           # => variable declared with capital letter in beginning
print(avgmarks)                                   # => variable incorrectly used in print statement
print(totalmarks)                                 # => variable incorrectly used in print statement
if Avgmarks>=80:
    print("grade is A")
elif Avgmarks>=60:
    print("grade is B")
elif Avgmarks>=40:
    print("grade is C")
else:
    print("You fail")