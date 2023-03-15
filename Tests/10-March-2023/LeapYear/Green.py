year = int(input("enter year"))
if year%4==0 and year%400==0 or year%100!=0 :
    print("Its a Leap Year")
else :
    print("Its not a leap year")