# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
print("Please enter your name")
username = input("Name: ")
# TODO: Ask the user for their age and store it in a variable
print(username + " How old are you?")
userage = input("Age: ")
# TODO: Print a greeting using the name and age variables
print("Hello " + username + " " +  userage + " Welcome to the world!!")
#-------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
print("what is the length of the rectangle?")
length = int(input('length:'))
# TODO: Ask the user for the width of a rectangle and store it as an integer
print("what is the width of the rectangle?")
width = int(input('width: '))
# TODO: Calculate the area of the rectangle
a = length * width 
# TODO: Print the result
print(a)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
print("What is the temperature in Cape town")
t = float(input('temperature: '))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
Fan = (t * 9/5 + 35)
# TODO: Print the result rounded to two decimal places
print(round(Fan, 2))
