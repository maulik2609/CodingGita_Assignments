#Question-19 --------------------------

marks = int(input("Enter Your Marks :"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=60:
    print("D")
else:
    print("F")

#Question-20 ------------------------

temp = int(input("Temprature :"))
if temp>40:
    print("Very Hot")
elif temp>=30 and temp<=39:
    print("Hot")
elif temp>=20 and temp<29:
    print("Warm")
else:
    print("Cold")

#Question-21 ---------------------------

signal_color = input("Traffic Signal Colour :")
if signal_color == "Red":
    print("Stop")
elif signal_color == "yellow":
    print("Wait")
elif signal_color == "Green":
    print("Go")
else:
    print("Invalid Colour")

#Question-22 -------------------------

electricity_use = int(input("Enter Usage of Electricity :"))
if electricity_use>=0 and electricity_use<=100:
    print("Low Usage")
elif electricity_use>=101 and electricity_use<=300:
    print("Medium Usage")
elif electricity_use>=301 and electricity_use<+500:
    print("High Usage")
else:
    print("Very High Usage")

#Question-23 -------------------------

age = int(input("Enter Age :"))
if age<5:
    print("Free Ticket")
elif age>=5 and age<=12:
    print("Child Ticket")
elif age>=13 and age<=59:
    print("Regular Ticket")
else:
    print("Senior Ticket")

#Question-24 ------------------------

weight = float(input("Enter Weight :"))
if weight<18.5:
    print("Underweight")
elif weight>=18.5 and weight<=24.9:
    print("Normal")
elif weight>=25 and weight<=29.9:
    print("Overweight")
else:
    print("Obese")

#Question-25 -----------------------------

number = int(input("Enter a Number :"))
if number == "1,3,5,7,8,10,12":
    print("31 Days")
elif number == "4,6,9,11":
    print("30 Days")
elif number == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")

#Question-26 --------------------------

num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))
operator = input("operator :")
if operator == "+":
    print(num_1+num_2)
elif operator == "-":
    print(num_1-num_2)
elif operator == "*":
    print(num_1*num_2)
elif operator == "/":
    print(num_1/num_2)

#Question-27 ----------------------------

num = int(input("Enter Number :"))
if num ==1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num ==3:
    print("Wednesday")
elif num ==4:
    print("Thrusday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Invalid Day")
