### 18.
What values will the following variables refer to?

python
name = "Rahul"
age = 18
city = "Patna"


Write your answer in this form:

text
name → ?
age → ?
city → ?

### Answer

name → "Rahul" 
age → 18 
city → "Patna"


### 19.
What is the final value of age?

python
age = 18
age = 19


Explain why.
### Answer
The final value of age is 19.

age = 18
age = 19

The second assignment replaces the previous value of 18.


### 20.
What is the final value of name?

python
name = "Rahul"
name = "Amit"
name = "Riya"

### Answer
The final value of name is "Riya".

name = "Rahul"
name = "Amit"
name = "Riya"

The latest assigned value is "Riya".


### 21.
Explain what happens in this program:

python
student_name = "Rahul"
student_age = 18

student_age = 19

### Answer

First, student_name is assigned "Rahul" and student_age is assigned 18.

Then, student_age is reassigned to 19.

So the final values are:

student_name → "Rahul"
student_age → 19


### 22.
What values will a, b, and c refer to?

python
a, b, c = 10, 20, 30

### Answer

a → 10 
b → 20 
c → 30


### 23.
What values will x, y, and z refer to?

python
x = y = z = 100

### Answer

x → 100 
y → 100 
z → 100


---

## D. Practical Problems

### 24.
Create variables for the following information:

- Your name
- Your age
- Your city

Use meaningful variable names.
### Answer
python
name = "Shrey" 
age = 19
city = "Ahmedabad"

print("Name:", name) 
print("Age:", age) 
print("City:", city)


### 25.
Create variables for:

- Student name
- Student roll number
- Student branch

Follow Python's recommended naming convention.
### Answer
python
student_name = "Rahul" 
student_roll_number = 101 
student_branch = "Computer Science" 

print("Student Name:", student_name) 
print("Roll Number:", student_roll_number) 
print("Branch:", student_branch)


### 26.
Write a program that assigns a value to a variable called marks, then reassigns a new value to marks.

Explain the value before and after reassignment.
### Answer
python
marks = 80 
print("Marks before reassignment:", marks) 

marks = 90 
print("Marks after reassignment:", marks)


### 27.
Use multiple assignment to create the following variables in one statement:

text
name → "Rahul"
age → 18
city → "Patna"

### Answer
python
name, age, city = "Rahul", 18, "Patna" 

print("Name:", name) 
print("Age:", age) 
print("City:", city)


### 28.
Use one statement to assign the value 0 to three variables:

text
x
y
z

### Answer
python
x = y = z = 0 

print("x:", x) 
print("y:", y) 
print("z:", z)


### 29.
The following code contains invalid variable names:

python
1student = "Rahul"
student name = "Rahul"
class = "B.Tech"


Rewrite all three using valid and meaningful variable names.
### Answer

python
student = "Rahul" 
student_name = "Rahul" 
class_name = "B.Tech" 

print("Student:", student) 
print("Student Name:", student_name) 
print("Class:", class_name)


### 30.
Create a small Python program that stores a student's name and age, reassigns the age to a new value, and then displays the current values. Use:
- A useful comment
- Meaningful variable names
- snake_case
- Reassignment

- ### Answer
- python
  # Store and display the student's current details
  student_name = "Rahul"
  student_age = 18
  student_age = 19

  print("Student Name:", student_name)
  print("Student Age:", student_age)
