#Question -37 ------------

s = input()

for i in range(len(s)):
    print(i, s[i])


#Question -38 ------------

s = input()
count = 0

for char in s:
    count = count + 1

print(count)


#Question -39 ------------

s = input()
vowels = 0
consonants = 0

for char in s.lower():
    if char == " ":
        continue

    if char in "aeiou":
        vowels = vowels + 1
    elif char.isalpha():
        consonants = consonants + 1

print("Vowels =", vowels)
print("Consonants =", consonants)


#Question -40 ------------

s = input()
target = input()
count = 0

for char in s:
    if char == target:
        count = count + 1

print(count)


#Question -41 ------------

s = input()
target = input()
position = -1

for i in range(len(s)):
    if s[i] == target:
        position = i
        break

if position == -1:
    print("Not Found")
else:
    print(position)


#Question -42 ------------

s = input()
upper = 0
lower = 0

for char in s:
    if char.isupper():
        upper = upper + 1
    elif char.islower():
        lower = lower + 1

print("Uppercase =", upper)
print("Lowercase =", lower)


#Question -43 ------------

s = input()

for char in s:
    print(char, ord(char))


#Question -44 ------------

s = input()
result = ""

for char in s:
    if char.lower() not in "aeiou":
        result = result + char

print(result)
