year=(int)(input("enter the year"))
if year%4==0 and year%400==0 and year%100==25:
    print(" yes leap year")
else:
    print(" not a leap year")