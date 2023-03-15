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
year=int(input("enter a year"))
check=(year %4 or 400)
if check %100 == 0:
    if check != 0 :
        print("it is a leap year")
    else:
        print("it is not a leap year")
else:
    print("not possible to tell, sorry")


