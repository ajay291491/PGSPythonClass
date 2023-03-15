English=int(input("enter marks for english"))
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