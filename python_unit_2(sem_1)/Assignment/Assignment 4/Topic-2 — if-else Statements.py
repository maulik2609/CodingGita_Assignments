#Question-9 ----------------------

num = int(input("Take a Number :"))
if num%2==0:
    print("Even")
elif num%2!=0:
    print("Odd")

#Question-10 ----------------------

marks = int(input("Enter Marks :"))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#Question-11 ----------------------

age = int(input("Enter your Age :"))
if age>=18:
    print("Adult")
else:
    print("Minor")

#Question-12 ----------------------

num = int(input("Pick A Number :"))
if num>0:
    print("Positive")
else:
    print("Non Positive")

#Question-13 ----------------------

num = int(input("Enter a Number :"))
if num%3==0:
    print("Divisible By 3")
else:
    print("Not Divisible By 3")

#Question-14 ----------------------

password = input("Enter Password :")
if password=="python123":
    print("Login Successful")
else:
    print("Invalid Password")

#Question-15 -----------------------

username = input("Enter Username :")
if username=="admin":
    print("Welcome Admin")
else:
    print("Invalid Username")

#Question-16 ------------------------

num1, num2 = int(input("Take Two Numbers :").split())
if num1>num2:
    print(num1)
elif num2>num1:
    print(num2)
else:
    print("Both are Equal") 

#Question-17 -------------------------

temp = int(input("Enter Temprature :"))
if temp>30:
    print("Hot")
else:
    print("Comfortable")

#Question-18 --------------------------

amount = int(input("Enter bill Amount :"))
if amount>=5000:
    print("Discount Available")
else:
    print("No Discount")
