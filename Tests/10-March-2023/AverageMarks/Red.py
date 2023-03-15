english=(int)(input("Enter your english marks"))
lang2=(int)(input("Enter your lang2 marks"))
maths=(int)(input("Enter your maths marks"))
science=(int)(input("Enter your science marks"))
social=(int)(input("Enter your social marks"))
Totalmarks=(english+lang2+maths+science+social)
Avgmarks=(Totalmarks/5)
print(avgmarks)
print(totalmarks
if Avgmarks>=80:
    print("grade is A")
elif Avgmarks>=60:
    print("grade is B")
elif Avgmarks>=40:
    print("grade is C")
else:
    print("You fail")