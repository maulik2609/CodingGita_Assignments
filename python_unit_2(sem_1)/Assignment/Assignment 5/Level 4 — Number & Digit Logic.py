#Question -23 ------------

n = int(input())
count = 0

for i in range(n):
    if n == 0:
        count = 1
        break
    count = count + 1
    n = n // 10

print(count)


#Question -24 ------------

n = int(input())
total = 0

for i in range(len(str(n))):
    digit = n % 10
    total = total + digit
    n = n // 10

print(total)


#Question -25 ------------

n = int(input())
product = 1

for i in range(len(str(n))):
    digit = n % 10
    product = product * digit
    n = n // 10

print(product)


#Question -26 ------------

n = int(input())
count = 0

for i in range(len(str(n))):
    digit = n % 10

    if digit % 2 == 0:
        count = count + 1

    n = n // 10

print(count)


#Question -27 ------------

n = int(input())
total = 0

for i in range(len(str(n))):
    digit = n % 10

    if digit % 2 == 0:
        total = total + digit

    n = n // 10

print(total)


#Question -28 ------------

n = int(input())
largest = 0

for i in range(len(str(n))):
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print(largest)


#Question -29 ------------

n = int(input())
smallest = 9

for i in range(len(str(n))):
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n = n // 10

print(smallest)


#Question -30 ------------

n = int(input())
reverse = 0

for i in range(len(str(n))):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse)


#Question -31 ------------

n = int(input())
original = n
reverse = 0

for i in range(len(str(n))):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


#Question -32 ------------

n, target = map(int, input().split())
count = 0

for i in range(len(str(n))):
    digit = n % 10

    if digit == target:
        count = count + 1

    n = n // 10

print(count)


#Question -33 ------------

n = int(input())

for i in range(len(str(n))):
    if n < 10:
        break
    n = n // 10

print(n)


#Question -34 ------------

n = int(input())
largest = 0
smallest = 9

for i in range(len(str(n))):
    digit = n % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    n = n // 10

print(largest - smallest)


#Question -35 ------------

n = int(input())
position = 1

for i in range(len(str(n))):
    digit = n % 10
    print(digit, position)

    position = position + 1
    n = n // 10


#Question -36 ------------

n = int(input())
original = n
total = 0

for i in range(3):
    digit = n % 10
    total = total + digit ** 3
    n = n // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

