#Question -62 ------------

n = int(input())
total = 0
highest = 0
lowest = 0

for i in range(n):
    expense = int(input())
    total = total + expense

    if i == 0:
        highest = expense
        lowest = expense
    else:
        if expense > highest:
            highest = expense
        if expense < lowest:
            lowest = expense

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)


#Question -63 ------------

n = int(input())
total = 0
highest = 0
lowest = 0

for i in range(n):
    marks = int(input())
    total = total + marks

    if i == 0:
        highest = marks
        lowest = marks
    else:
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks

average = total / n

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)


#Question -64 ------------

n = int(input())
statuses = input().split()
present = 0
absent = 0

for status in statuses:
    if status == "P":
        present = present + 1
    elif status == "A":
        absent = absent + 1

attendance = present / n * 100

print("Present:", present)
print("Absent:", absent)
print("Attendance:", round(attendance, 2), "%")


#Question -65 ------------

n = int(input())
units_list = list(map(int, input().split()))
total = 0
above_10 = 0

for units in units_list:
    total = total + units

    if units > 10:
        above_10 = above_10 + 1

print("Total Units:", total)
print("Days Above 10:", above_10)


#Question -66 ------------

n = int(input())
prices = list(map(int, input().split()))
total = 0
above_1000 = 0

for price in prices:
    total = total + price

    if price > 1000:
        above_1000 = above_1000 + 1

print("Total Bill:", total)
print("Products Above 1000:", above_1000)


#Question -67 ------------

n = int(input())
attempts = input().split()
successful = 0
failed = 0

for attempt in attempts:
    if attempt == "success":
        successful = successful + 1
    elif attempt == "failed":
        failed = failed + 1

rate = successful / n * 100

print("Successful:", successful)
print("Failed:", failed)
print("Success Rate:", rate, "%")

