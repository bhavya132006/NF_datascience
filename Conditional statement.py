#Write a program to check whether a year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


#Write a program to find the largest among three numbers using nested conditional statements. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print("Largest number is", a)
    else:
        print("Largest number is", c)
else:
    if b > c:
        print("Largest number is", b)
    else:
        print("Largest number is", c)


#Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or special character. 
ch = input("Enter a character: ")
if ch >= 'A' and ch <= 'Z':
    print("Uppercase Letter")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase Letter")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Character")

  
#Write a program to calculate electricity bill using different unit slabs.
units = int(input("Enter electricity units: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)
print("Electricity Bill =", bill)


#Write a program to determine whether a triangle is Equilateral, Isosceles, or Scalene. 
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


#Write a program to create a simple calculator using if-elif-else. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == '+':
    print("Result =", num1 + num2)
elif op == '-':
    print("Result =", num1 - num2)
elif op == '*':
    print("Result =", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid Operator")


 #Write a program to calculate income tax according to salary ranges.
salary = float(input("Enter annual salary: "))

if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print("Income Tax =", tax)


#Write a program to check login authentication using username and password conditions. 
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

# Write a program to determine whether a point lies in First quadrant, Second quadrant, Third quadrant, Fourth quadrant, On axis, or At origin. 
x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))
if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
elif x == 0 and y == 0:
    print("At Origin")
else:
    print("On Axis")

# Write a program to assign grades based on marks and display distinction for high scores. 
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A+")
    print("Distinction")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
