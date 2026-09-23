#Question-60 ------------------------

name = input()


marks1, marks2, marks3 = input().split()

m1 = int(marks1)
m2 = int(marks2)
m3 = int(marks3)

total = m1 + m2 + m3
average = total / 3

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")

#Question-61 ------------------------

degree= input()
Batch= input()
Branch = input()
Roll = int(input())

print(f"Degree : {degree}")
print(f"Batch : {Batch}")
print(f"Branch : {Branch}")
print(f"Roll Number: {Roll}")

#Question-62 ------------------------

name= input("Name :").split(" ")
first_word,second_word,third_word= name
print(f"{first_word}.{third_word}")

#Question-63 ------------------------

word= "Python is Very Powerful"
First_word= word[0:6]
Last_word= word[15:24]
print(f"First word :{First_word}")
print(f"Last word : {Last_word}")

#Question-65 -------------------------

character= input("Character :")
code= ord(character)
print(code)

#Question-66 -------------------------

product= "Pen"
price= 20
quantity= 5
discount= 10
discount_percentage= discount/100

subtotal = price*quantity
discount = subtotal*discount_percentage / 100 *100
final_Total = subtotal - discount

print(f"Product : {product}\n Price : {price}\n Quantity : {quantity}\n Subtotal : {subtotal}\n Discount : {discount}\n Final Total : {final_Total}")
