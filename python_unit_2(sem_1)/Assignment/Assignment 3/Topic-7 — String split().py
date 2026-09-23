#Question-33 -------------------

text = "Python is easy"
print(text.split()) #Output = ['Python', 'is', 'easy']

#Question-34 -------------------

data = "apple,banana,mango"
print(data.split(",")) #Output = ['apple', 'banana', 'mango']

#Question-35 --------------------
text = "Python is easy"
print(text.split(",")) #Output = ['Python', 'is', 'easy']

#Question-36 -------------------
name= "Rahul Kumar Sharma"
print(name.split(""), sep="\n")

#Question-37 ------------------

name= input("First Name") #Rahul
name2 = input("Last Name") #Kumar
FullName= name + name2
print(FullName) #Output = Rahul Kumar

#Question-38 ------------------

num1, num2, num3 = input().split()
total_sum = int(num1) + int(num2) + int(num3)

#Question-39 ------------------

Name= input("Enter Your Name :")
Age= input("Enter Your Age :")
Course= input("Enter Your Course :")
City= input("Enter Your City :")

print(f"Name : {Name}\n Age : {Age}\n Course : {Course}\n City : {City}")

#Question-40 -------------------

email = input("Enter email address: ")

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)

#Question-41 ----------------------

word= input("Word")
firstword, lastword = word.split(".")

print("First Word", firstword)
print("Last Word", lastword)
