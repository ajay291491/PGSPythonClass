# Date : 21-07-2023
# 
# > Baic Input and Output
# my_name = input("Enter Your name : ")
# my_grade = int(input("Enter Your Grade : ")) 
# print("Hello", my_name, "Your are Studying at Grade : ", my_grade)
# print("Hello {}, Your are Studying at Grade : {}".format(my_name, my_grade))
#
#
#
# Date : 28-07-2023
# > Students should complete this program for first 20 mins
#
# * Write a program to collect an order for your online fruit Shop *
# - You should give option for the list of fruits available
# - Quantity of the Fruits available
# - print a message by what time your give the Fruit with its name, time,
# quantity, location
#
# Example
# Fruit Options Available :
# Apple  - 10
# Orange - 15
# Grapes - 100
# Kiwi   - 25
#
# Choose Your Fruit :
# Choose Quantity :
# Place to Deliver :
#
# print("We will Deliver 5 Apple by 20-07-2023 05:00 PM at Madanapalli")
#

# # Conditionals - Only If
# fruit_name = input("Enter Your Fruit name : ")  # -> User Input
# if fruit_name == "orange":                      # Condition
#     print("{} is available in stock".format(fruit_name))

# Conditionals - if  else

# fruit_name = input("Enter Your Fruit name : ")
# if fruit_name == "orange" :
#     print("{} is available in stock".format(fruit_name))
# else:
#     print("{} is not available in stock".format(fruit_name))

# Conditionals - if elif else

# fruit_name = input("Enter Your Fruit name : ")
# if fruit_name == "orange" :
#     print("{} is available in stock".format(fruit_name))
# elif fruit_name == "apple" :
#     print("{} is available in stock".format(fruit_name))
# elif fruit_name == "grapes" :
#     print("{} is available in stock".format(fruit_name))
# else:
#     print("{} is not available in stock".format(fruit_name))

# Excercise
# * Write a program to collect an order for your online fruit Shop *
#
# - You should give option for the list of fruits available
# - Quantity of the Fruits available
# - Check if the fruits available in your stock
# - if available - print a message by what time your give the Fruit with its name, time, quantity, location
# - if not available - you should print a message to them it's not available
# - You must have at least 3 types of fruits available in your stock
#
#
# Example
# Fruit Options Available :
# Apple  - 10
# Orange - 15
# Grapes - 100
# Kiwi   - 25


# Conditionals - if  else with or

# fruit_name = input("Enter Your Fruit name : ")
# if fruit_name == "orange"  or fruit_name == "apple":
#     print("{} is available in stock".format(fruit_name))
# else:
#     print("{} is not available in stock".format(fruit_name))

# Conditionals - if  else with and
# fruit_name = input("Enter Your Fruit name : ")
# quantity = int(input("Enter Your Fruit quantity : "))
# if fruit_name == "orange" and quantity < 10:
#     print("{} is available in stock".format(fruit_name))
# else:
#     print("{} is not available in stock".format(fruit_name))



# 18-Aug-2023 : Built-in Functions
# These are functions that are provided by Python itself, as mentioned in the previous response. They are available for direct use without requiring any import.

type_of_input = type(123)
print(type_of_input)

min_value = min(-10, 10, 20, -100)
print(min_value)

max_value = max(-10, 10, 20, -100)
print(max_value)

my_list = range(10)
for number in my_list:
    print(number)

sample_small_name = "peepal grove school "
print(sample_small_name.upper())

sample_cap_name = "PEEPAL GROVE SCHOOL"
print(sample_cap_name.lower())

sample_cap_name = "PEEPAL GROVE SCHOOL"
print(len(sample_cap_name))

from datetime import datetime
current_time= datetime.now()
print(current_time)
print(current_time.month)

# Work : Write a Program as below
# - Check given input is a string
#  -  if it is a string convert them into capital letter



# my_input = input("Enter Your Input : ")
# if type(my_input) is str:
#     print(my_input.upper())

# Work : Write a Program as below
# - Write a program to enter an integer as an input
# check the number is an even or odd number
# if even number multiply it by 10 and provide the result
# if odd number divide by 3


# my_number = int(input("Enter Your number : "))
# if my_number % 2 == 0:
#     print(my_number * 10)
# else:
#     print(my_number / 3)


# Work : Write a Program as below
# - Write a program to enter an integer as an input
# check the number is an even or odd number
# if even number multiply it by 10 and provide the result
# if odd number divide by 3


# 18-Aug-2023 : List









# * Write a program to collect an order for your online fruit Shop *
#

# - You should give option for the list of fruits available
# - Quantity of the Fruits available

print("Apple = 80")
print("Grapes = 50")
print("Orange = 50")
fruit_name     = input("Enter Your Fruit name : ")
fruit_quantity = int(input("Enter Your Quantity : "))
if fruit_name == "Apple":
    if fruit_quantity <= 80:
        print("Fruit - {} is in stock".format(fruit_name))
    else:
        print("Fruit - {} is not in stock".format(fruit_name))
elif fruit_name == "Orange" and fruit_quantity <= 50:
    print("Fruit - {} is in stock".format(fruit_name))
elif fruit_name == "Grapes" and fruit_quantity <= 50:
    print("Fruit - {} is in stock".format(fruit_name))
else:
    print("{} is not available".format(fruit_name))


# - if not available - you should print a message to them it's not available
# - You must have at least 3 types of fruits available in your stock
