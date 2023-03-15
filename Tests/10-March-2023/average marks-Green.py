en = int(input("enter marks in english out of 100 : "))
ss = int(input("enter marks in social studies out of 100 : "))
sci = int(input("enter marks in science out of 100 : "))
m = int(input("enter marks in math out of 100 : "))
ln = int(input("enter marks in 2nd lang out of 100: "))

 
ttl = en+ss+sci+m+ln
av = ttl/5

print (av, "this is your average marks")
print (ttl, "this is your total marks") 

if av>=80:
    print( " Your grade is a" )
elif av>=60:
    print( " Your grade is b" )
elif av>=40:
    print( " Your grade is c" )
else:
    print("you are a failure")