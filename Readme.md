### What is Programming ?
Programming is a process of designing and writing computer programs that make the computer to perform certain tasks .
It is a form of communication that uses symbols to represent instructions for making a machine do what you want.

Programming enables people to solve practical problems by breaking them down into a series of logical steps, known as algorithms or programs.
Application developers can use any number of programming languages to write applications for specific kinds of computers, like supercomputers, laptops, and
smartphones.

### What are the Benifits of programming ?

- Computer programming can be used to create innovative and functional software.
- Computers can also be programmed to perform specific tasks using mathematical algorithms and logic
- It can also be used to create websites, games, and other digital content.

In this way, computer programs make it possible for people to access a wide range of entertainment and information online

Below are few examples of applications created by software 
- Taxi booking apps 
- Google maps
- Bank websites 
- School website

### What we Studied so far ?
variables      : Variable in a program gives the data to the computer for processing a specific logic

_Example_ 
```
my_input = "Tom"
```
Input Function : Input() is the way to accept the values external to the program

_Example_
```
name = input("Please Enter Your Name : ")
```
print Function : Print() is the way to standard output from a program into a device or file.

_Example_
```
name = input("Please Enter Your Name : ")
print("Your Name\t: " + name)
```

Logic          : Logic is a set of instruction we are grouped together to perform a task

_Example_
```
name = input("Please Enter student Name : ")
if name in programming_group:
    print("Student : {} is a member of the programming group".format(name))
```


### Conditionals
To check a value is True of False and then execute a bunch of statements based on that

#### if only 
This will help to execute set of instructions if the conditions is true

_Example_
```
my_number = 48
remaider_value =   my_number % 2
if remaider_value == 0:
    print("Number : {} is an even number".format(my_number))
```


#### if else:
This will help to execute set of instructions if the conditions is true as well as false.

_Example_
```
my_number = input("Please Enter your number : ")
remaider_value =   int(my_number) % 2
if remaider_value == 0:
    print("Number : {} is an even number".format(my_number))
else: 
    print("Number : {} is an odd number".format(my_number))
```

#### if elif else:
This will help to execute set of instructions if multiple conditions are true as well as false.

_Example_
```
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
```
###### NOTE :  Test planned for 03-March-2023 (2 Programs & 40 Minutes)

What we are planning to Study next ?
List        :
for Loops   :
Range()     :
Dictionary  :
while loop  :
""" 
