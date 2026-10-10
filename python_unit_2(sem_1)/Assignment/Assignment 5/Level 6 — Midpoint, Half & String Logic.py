#Question -45 ------------

s = input()
middle = len(s) // 2

print(s[middle])


#Question -46 ------------

s = input()
middle = len(s) // 2

print("First Half:", s[:middle])
print("Second Half:", s[middle:])


#Question -47 ------------

s = input()
length = len(s)
first = ""
second = ""
middle = ""

for i in range(length):
    if length % 2 == 1 and i == length // 2:
        middle = s[i]
    elif i < length // 2:
        first = first + s[i]
    else:
        second = second + s[i]

print("First Half:", first)

if length % 2 == 1:
    print("Middle:", middle)

print("Second Half:", second)


#Question -48 ------------

s = input()
half = len(s) // 2
equal = True

for i in range(half):
    if s[i] != s[i + half]:
        equal = False

if equal:
    print("Equal Halves")
else:
    print("Different Halves")


#Question -49 ------------

s = input()
symmetric = True

for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        symmetric = False

if symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")


#Question -50 ------------

s = input()

for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end="")


#Question -51 ------------

s = input()
even_count = 0
odd_count = 0

for i in range(len(s)):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even Index =", even_count)
print("Odd Index =", odd_count)


#Question -52 ------------

s = input()
result = ""

for i in range(0, len(s), 2):
    result = result + s[i + 1] + s[i]

print(result)

