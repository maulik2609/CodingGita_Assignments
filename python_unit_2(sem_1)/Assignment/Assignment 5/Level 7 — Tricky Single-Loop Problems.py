#Question -53 ------------

n = int(input())
largest = -1
second_largest = -1

for i in range(len(str(n))):
    digit = n % 10

    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit < largest and digit > second_largest:
        second_largest = digit

    n = n // 10

print(second_largest)


#Question -54 ------------

s = input()
current = 0
best = 0
previous = ""

for char in s:
    if char == previous:
        current = current + 1
    else:
        current = 1
        previous = char

    if current > best:
        best = current

print(best)


#Question -55 ------------

s = input()
target = input()
count = 0
length = 0

for char in s:
    length = length + 1

    if char == target:
        count = count + 1

frequency = count / length * 100

print("Count =", count)
print("Frequency =", round(frequency, 2), "%")


#Question -56 ------------

n = int(input())
total = 0

for i in range(len(str(n))):
    digit = n % 10
    total = total + digit
    print(total)
    n = n // 10


#Question -57 ------------

n = int(input())
even = 0
odd = 0

for i in range(len(str(n))):
    digit = n % 10

    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    n = n // 10

if even > odd:
    print("More Even Digits")
elif odd > even:
    print("More Odd Digits")
else:
    print("Equal")


#Question -58 ------------

n = int(input())
total = 0
sign = 1

for i in range(len(str(n))):
    digit = n % 10
    total = total + sign * digit
    sign = sign * -1
    n = n // 10

print(total)


#Question -59 ------------

total = 0

for i in range(1, 6):
    total = total + i * 2
    print(total)


#Question -60 ------------

count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1

print(count)


#Question -61 ------------

total = 0

for i in range(1, 6):
    total = total + i

print(total)
