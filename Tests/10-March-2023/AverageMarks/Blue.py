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