"""
Assessment & Comments
- User unable to identify which subject they need to provide marks
- english=int(input("enter marks"))  can be written as english=int(input("enter marks for the Subject English : "))
- print statement can be written better

 * Marks *
Working program : 5/5
Code Quality    : 2/3
Comments used   : 1/2
Total           : 8/10
"""

english=int(input("enter marks"))
lang=int(input("enter marks"))
Math=int(input("enter marks"))
Science=int(input("enter marks"))
SocialStudies=int(input("enter marks"))
average=((english + lang + Math + Science + SocialStudies)/5)
print(average)
if average >= 80 :
    print("A grade")
elif average >= 60 :
    print("b grade")
elif average >= 40 :
    print("c grade")
else:
    print("fail")