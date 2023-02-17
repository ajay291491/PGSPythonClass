# Date  : 16-Sep-2022
"""
print('hello ' + name)
print("Hello " + name + " How are you !!")
"""

# Date  : 30-Sep-2022
"""
# Using Tab (\t) with print()
name = input("Please Enter Your Name : ")
place = input("What is your location : ")
print("Your Name\t: " + name)
print("Your Location\t: " + place)
"""

"""
# Using Tab(\t) and newline (\n) with print()
name = input("Please Enter Your Name : ")
place = input("What is your location : ")
print("Your Name\t: " + name + "\n" + "Your Location\t: " + place )
"""

"""
# Using format() with print()
name = input("Please Enter Your Name : ")
place = input("What is your location : ")
print("Your Name\t: {}\nYour Location\t: {}".format(name, place))
"""

"""
# Using format() with multiple print()
name = input("Please Enter Your Name : ")
place = input("What is your location : ")
print("Your Name\t: {}".format(name))
print("Your Name\t: {}".format(place))
"""
"""
print('Understanding variables')
"""

# Class Date 27-jan-2023
"""
# if condition
favorite_sports = input("Please Enter Your favorite sports : ")
if favorite_sports == 'cricket':
    print('my favorite sports is : {}'.format(favorite_sports))
"""
"""
# if..else condition
favorite_sports = input("Please Enter Your favorite sports : ")
if favorite_sports == 'cricket':
    print('my favorite sports is : {}'.format(favorite_sports))
else:
    print('This is not my favorite sports : {}'.format(favorite_sports))
"""

"""
# if..elif..else condition
favorite_sports = input("Please Enter Your favorite sports : ")
if favorite_sports == 'cricket':
    print('cricket is my favorite sports')
elif favorite_sports == 'football':
    print('football is my favorite sports')
else:
    print('This is not my favorite sports : {}'.format(favorite_sports))
"""

#-------------------------------------------------------------------------------------------------------
#               Excercise : 02-Feb-2023
#-------------------------------------------------------------------------------------------------------
"""
#my_input = 2
#my_input = 2.5
my_input = "Tom"

if isinstance(my_input, int):
    print('You have Entered an Intiger : {}'.format(my_input))
elif isinstance(my_input, str):
    print('You have Entered an String : {}'.format(my_input))
elif isinstance(my_input, float):
    print('You have Entered an Float : {}'.format(my_input))
else:
    print("Invalid entry")
"""
#-------------------------------------------------------------------------------------------------------
#               Revision : 17-Feb-2023
#-------------------------------------------------------------------------------------------------------
"""
First thing : Everyone should have a notebook and a pen and must revisit it before come for next class 

What is Programming ?
Programming is a process of designing and writing computer programs that make 
the computer to perform certain tasks . 
It is a form of communication that uses symbols to represent instructions for 
making a machine do what you want.

Programming enables people to solve practical problems by breaking them down into 
a series of logical steps, known as algorithms or programs. 
Application developers can use any number of programming languages to write 
applications for specific kinds of computers, like supercomputers, laptops, and 
smartphones.

Benifits ?

- Computer programming can be used to create innovative and functional software.
- Computers can also be programmed to perform specific tasks using mathematical algorithms and logic
- It can also be used to create websites, games, and other digital content. 

In this way, computer programs make it possible for people to access a wide range of entertainment and information online

Example : taxi booking, google maps, bank websites, school website

What we Studied so far ? 
Input Function : Input() is the way to accept the values external to the program
print Function : Print() is the way to standard output from a program into a device or file.
variables      : Variable in a program gives the data to the computer for processing a specific logic
Logic          : is is a set of instruction we are grouped together to perform a task 
Conditionals   : To check a value is True of False and then execute a bunch of statements based on that

# Test planned for 03-March-2023 (3 Programs & 1 Hour)

What we are planning to Study next ?
List        : 
for Loops   : 
Range()     :
Dictionary  : 
while loop  : 
"""



#-------------------------------------------------------------------------------------------------------
#               Excercise : 17-Feb-2023 (String variable to List)
#-------------------------------------------------------------------------------------------------------
# Use Range fucntion to explain first
# Show what is list
my_list = range(100)
print(my_list)
for number in my_list:
    print(number)
