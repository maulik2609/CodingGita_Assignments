[2:58 pm, 8/9/2026] Aditya: #TOPIC 1 : VARIABLES AND VARIABLES NAMING 

# Question 1 ------------------------------------------------------------------------------------------------

name = "Raju"
print("Name:", name)

# Question 2 ------------------------------------------------------------------------------------------------

student_name = "Aman"
print("Student Name:", student_name)

# Question 3 -----------------------------------------------------------------------------------------------

student_name = "Rahul"
print("Student Name:", student_name)

# Question 4 -----------------------------------------------------------------------------------------------

student_name = "Ravi"
print("Student Name:", student_name)

# Question 5 ----------------------------------------------------…
[2:59 pm, 8/9/2026] Aditya: # TOPIC 1 : TYPE CASTING 

# Question 1 -----------------------------------------------------------------------------------------------

age = "25"
age=int(age)

print(age)
print(type(age))

# Question 2 -----------------------------------------------------------------------------------------------

marks="75.5"
marks=float(marks)

print(marks)
print(type(marks))

# Question 3 -----------------------------------------------------------------------------------------------

number = 50
number = float(number)

print(number)
print(type(number))

# Question 4 -----------------------------------------------------------------------------------------------

marks = 85.9
marks = int(marks)

print(marks)
print(type(marks))

# Question 5 -----------------------------------------------------------------------------------------------

roll_number=101
roll_number=str(roll_number)

print(roll_number)
print(type(roll_number))

# Question 6 -----------------------------------------------------------------------------------------------

age = "18"
age=int(age)

print(age)
print(type(age))

#------------------------

marks="92.5"
marks=float(marks)

print(marks)
print(type(marks))

#-------------------------

roll_number=100
roll_number=str(roll_number)

print(roll_number)
print(type(roll_number))

# ------------------------

marks = 45.8
marks = int(marks)

print(marks)
print(type(marks))

# Question 7 -----------------------------------------------------------------------------------------------

a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))

# Question 8 -----------------------------------------------------------------------------------------------

age = 19
new_age = age + 1

print("Age:", new_age)
#the value of the variable "age" is in string datatype

# Question 9 -----------------------------------------------------------------------------------------------

marks="85"
marks=int(marks)
marks += 5

print("Final marks:", marks)

# Question 10 -----------------------------------------------------------------------------------------------

price="1499.50"
delivery_charges=99.50

price=float(price)
price += delivery_charges

print("Toatal amount:" , price)


# TOPIC 2 : ARITHMETIC OPERATORS

# Question 11 -----------------------------------------------------------------------------------------------

a=20
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Question 12 -----------------------------------------------------------------------------------------------

a = 17
b = 5

print(a / b) # the output is 3.4
print(a // b) # the output is 3
print(a % b) # the output is 2

# a / b performs normal division, so it returns the floating-point result 3.4.
#a // b performs floor division, so it returns only the whole number 3, while a % b returns the remainder after division, which is 2.

# Question 13 -----------------------------------------------------------------------------------------------

result = 10 + 5 * 2
print(result)

# to being addition first

result = (10 + 5) * 2
print(result)

# Question 14 -----------------------------------------------------------------------------------------------

result = 20 - 4 * 3 + 2
print(result) #output is 10

# after rewrite it 

result = (20 - (4 * 3)) + 2
print(result) 

# Question 15 -----------------------------------------------------------------------------------------------

print(2 ** 3) # --> 8
print(3 ** 2) # --> 9
print(10 ** 2) # -> 100

# area of the square

side=5
area_of_square= 5**2

print(area_of_square)

# Question 16 -----------------------------------------------------------------------------------------------

notebook = 80
pen = 20
pencil = 10
total_amount= notebook+pen+pencil

print(total_amount)

# Question 17 -----------------------------------------------------------------------------------------------

notebook = 50
pen = 15
calculator =500

notebook_cost= 3*notebook
pen_cost= 2*pen
calculator_cost= 1*calculator
total_bill= notebook_cost + pen_cost + calculator_cost

print("Notebook cost:", notebook_cost)
print("Pen cost:", pen_cost)
print("Calculator cost:", calculator_cost)
print("Total bill:", total_bill)

# Question 18 -----------------------------------------------------------------------------------------------

total_students= 47

complete_groups= 47//5
student_left_over= 47%5

print("Complete groups:", complete_groups)
print("students Left:", student_left_over)

# Question 19 -----------------------------------------------------------------------------------------------

python= 85
mathematics= 78
physics= 92

total_marks= python + mathematics + physics
average_mrks= total_marks/3

print("Total marks :" , total_marks)
print( "average marks :" , average_mrks)

# Question 20 -----------------------------------------------------------------------------------------------

English = 78
Mathematics = 85
Python = 92
Physics = 81
Chemistry = 74

#Each subject is out of 100.

total_marks= English + Mathematics + Python + Physics + Chemistry
percentage= (total_marks/500)*100

print(total_marks)
print(percentage)

# TOPIC 3: Digit Extraction using % and //

# Question 21 -----------------------------------------------------------------------------------------------

number = 583

ones_digit = number % 10

print("Ones Digit:", ones_digit)

# Question 22 -----------------------------------------------------------------------------------------------

number = 583

tens_digit = (number // 10) % 10

print("Tens Digit:", tens_digit)

# Question 23 -----------------------------------------------------------------------------------------------

number = 583

hundreds_digit = number // 100

print("Hundreds Digit:", hundreds_digit)

# Question 24 -----------------------------------------------------------------------------------------------

number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones Digit:", ones)
print("Tens Digit:", tens)
print("Hundreds Digit:", hundreds)

# Question 25 -----------------------------------------------------------------------------------------------

number = 5829

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

print("Ones Digit:", ones)
print("Tens Digit:", tens)
print("Hundreds Digit:", hundreds)
print("Thousands Digit:", thousands)

# Question 26 -----------------------------------------------------------------------------------------------

number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

sum_of_digits = ones + tens + hundreds

print("Sum of Digits:", sum_of_digits)

# Question 27 -----------------------------------------------------------------------------------------------

number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

sum_of_digits = ones + tens + hundreds + thousands

print("Sum of Digits:", sum_of_digits)

# Question 28 -----------------------------------------------------------------------------------------------

number = 234

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

product = ones * tens * hundreds

print("Product of Digits:", product)

# Question 29 -----------------------------------------------------------------------------------------------

number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

reversed_number = (ones * 100) + (tens * 10) + hundreds

print("Original Number:", number)
print("Reversed Number:", reversed_number)

# Question 30 -----------------------------------------------------------------------------------------------

number = 4726

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000

reversed_number = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands

print("Original Number:", number)
print("Reversed Number:", reversed_number)

# Question 31 -----------------------------------------------------------------------------------------------

number = 5834

thousands = (number // 1000) * 1000
hundreds = ((number // 100) % 10) * 100
tens = ((number // 10) % 10) * 10
ones = number % 10

print("Thousands Place:", thousands)
print("Hundreds Place:", hundreds)
print("Tens Place:", tens)
print("Ones Place:", ones)

# Question 32 -----------------------------------------------------------------------------------------------

number = 583

hundreds = number // 100
ones = number % 10

difference = hundreds - ones

print("Difference:", difference)

# Question 33 -----------------------------------------------------------------------------------------------

number = 583

ones = number % 10

print("Ones Digit:", ones)

# Question 34 -----------------------------------------------------------------------------------------------

number = 9365

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)

# Question 35 -----------------------------------------------------------------------------------------------

hundreds = 5
tens = 8
ones = 3

number = (hundreds * 100) + (tens * 10) + ones

print("Number:", number)

# TOPIC 4: Real-Life Arithmetic Problems

# Question 36 -----------------------------------------------------------------------------------------------

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

# Question 37 -----------------------------------------------------------------------------------------------

length = 15
width = 8

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

# Question 38 -----------------------------------------------------------------------------------------------

radius = 7
pi = 3.14

area = pi * radius * radius

print("Area of Circle:", area)

# Question 39 -----------------------------------------------------------------------------------------------

celsius = 35

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)

# Question 40 -----------------------------------------------------------------------------------------------

seconds = 367

minutes = seconds // 60
remaining_seconds = seconds % 60

print("Minutes:", minutes)
print("Seconds:", remaining_seconds)

# Question 41 -----------------------------------------------------------------------------------------------

total_seconds = 7384

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

# Question 42 -----------------------------------------------------------------------------------------------

basic_salary = 25000
hra = 5000
travel_allowance = 2500
tax_deduction = 3000

gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - tax_deduction

print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

# Question 43 -----------------------------------------------------------------------------------------------

distance = 120
mileage = 20
fuel_price = 100

fuel_required = distance / mileage
total_cost = fuel_required * fuel_price

print("Fuel Required:", fuel_required, "litres")
print("Total Fuel Cost:", total_cost)

# Question 44 -----------------------------------------------------------------------------------------------

price = "2500"
discount = "10"

price = float(price)
discount = float(discount)

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)

# TOPIC 5: Type Casting + Arithmetic Operators

# Question 45 -----------------------------------------------------------------------------------------------

price = "1200"
quantity = "4"

price = int(price)
quantity = int(quantity)

total_price = price * quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total Price:", total_price)

# Question 46 -----------------------------------------------------------------------------------------------

python_marks = "85"
math_marks = "78"
physics_marks = "91"

python_marks = int(python_marks)
math_marks = int(math_marks)
physics_marks = int(physics_marks)

total_marks = python_marks + math_marks + physics_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Question 47 -----------------------------------------------------------------------------------------------

price = "1500"
quantity = "2"
tax_rate = "5"

price = int(price)
quantity = int(quantity)
tax_rate = int(tax_rate)

subtotal = price * quantity
tax_amount = (subtotal * tax_rate) / 100
final_bill = subtotal + tax_amount

print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)

# Question 48 -----------------------------------------------------------------------------------------------

price = 2000
discount = 15
gst = 18

discount_amount = (price * discount) / 100
price_after_discount = price - discount_amount
gst_amount = (price_after_discount * gst) / 100
final_price = price_after_discount + gst_amount

print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)

# Question 49 -----------------------------------------------------------------------------------------------

price = "500"
quantity = 3

price = int(price)

total = price * quantity

print("Total:", total)

# Question 50 -----------------------------------------------------------------------------------------------

marks1 = "80"
marks2 = "75"
marks3 = "90"

marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total = marks1 + marks2 + marks3

print("Total Marks:", total)

# TOPIC 6: Output Prediction and Conceptual Practice

# Question 51 -----------------------------------------------------------------------------------------------

a = "50"
b = int(a)

print(a)
print(b)
print(type(a))
print(type(b))

# Output:
# 50
# 50
# <class 'str'>
# <class 'int'>

# Question 52 -----------------------------------------------------------------------------------------------

number = 99.99
result = int(number)

print(number)
print(result)

# Output:
# 99.99
# 99

# The int() function removes the decimal part and keeps only the integer part.

# Question 53 -----------------------------------------------------------------------------------------------

a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# Output:
# 17
# 7
# 60
# 2.4
# 2
# 2

# Question 54 -----------------------------------------------------------------------------------------------

print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))

# Output:
# 20
# 30
# 7.0
# 2.5

# Parentheses are evaluated first, so they change the order of calculation.

# Question 55 -----------------------------------------------------------------------------------------------

number = 684

a = number % 10
b = number // 10
c = b % 10
d = number // 100

print(a)
print(c)
print(d)

# Output:
# 4
# 8
# 6

# a = Ones Digit
# c = Tens Digit
# d = Hundreds Digit
# TOPIC 7: Mixed Debugging

# Question 56 -----------------------------------------------------------------------------------------------

student_name = "Ravi"
marks = "85"

marks = int(marks)
total = marks + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))

# Question 57 -----------------------------------------------------------------------------------------------

number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)

# Question 58 -----------------------------------------------------------------------------------------------

price = "2000"
discount = "15"

price = int(price)
discount = int(discount)

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)

# Question 59 -----------------------------------------------------------------------------------------------

student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"

marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total = marks1 + marks2 + marks3
average = total / 3

print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))

# Question 60 -----------------------------------------------------------------------------------------------

# Part A — Number Analysis

number = 5836

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

sum_of_digits = thousands + hundreds + tens + ones

reversed_number = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)

# Part B — Product Billing

price = "1250"
quantity = "4"
discount = "10"

price = int(price)
quantity = int(quantity)
discount = int(discount)

subtotal = price * quantity
discount_amount = (subtotal * discount) / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
