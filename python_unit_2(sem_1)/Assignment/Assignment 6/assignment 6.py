
#Question - no. 1 ------------
n = 5
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

#Question - no. 2 ------------
rows = 3
columns = 6
for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()

#Question - no. 3 ------------
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

#Question - no. 4 ------------
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#Question - no. 5 ------------
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

#Question - no. 6 ------------
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(64 + i), end="")
    print()

#Question - no. 7 ------------
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

#Question - no. 8 ------------
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end="")
        if j < i - 1:
            print(" ", end="")
        num = num + 1
    print()

#Question - no. 9 ------------
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j + 1) % 2, end="")
        if j < i:
            print(" ", end="")
    print()

#Question - no. 10 ------------
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#Question - no. 11 ------------
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#Question - no. 12 ------------
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

#Question - no. 13 ------------
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

#Question - no. 14 ------------
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

#Question - no. 15 ------------
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

#Question - no. 16 ------------
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

#Question - no. 17 ------------
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

#Question - no. 18 ------------
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(n):
        print("*", end="")
    print()

#Question - no. 19 ------------
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

#Question - no. 20 ------------
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
        if j < i:
            print(" ", end="")
    print()

#Question - no. 21 ------------
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

#Question - no. 22 ------------
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()

#Question - no. 23 ------------
n = 5
for i in range(n):
    for j in range(n - i, n + 1):
        print(chr(64 + j), end=" ")
    print()

#Question - no. 24 ------------
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#Question - no. 25 ------------
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#Question - no. 26 ------------
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

#Question - no. 27 ------------
n = 5
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()

#Question - no. 28 ------------
n = 5
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()

#Question - no. 29 ------------
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="")
        if j < n:
            print(" ", end="")
    print()

#Question - no. 30 ------------
n = 5
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(1, i + 1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    print()
