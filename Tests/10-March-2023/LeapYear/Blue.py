"""
Team : Blue (Surya Shankar, Jakkula Sree Sahasra Krishna, Reethu Reddy Yakasiri)

Assessment & Comments

. Good
- Working program, but the calculations are partially right
- Error handling is impressive

. Areas to Improve
- Calculation can be made better

 * Marks *
Working program : 4/5
Code Quality    : 2/3
Comments used   : 2/2
Total           : 9/10
"""

year=int(input("enter a year"))
check=(year %4 or 400)
if check %100 == 0:
    if check != 0 :
        print("it is a leap year")
    else:
        print("it is not a leap year")
else:
    print("not possible to tell, sorry")