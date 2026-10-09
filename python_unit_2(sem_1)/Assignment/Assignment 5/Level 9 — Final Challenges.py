#Question -68 ------------

n = int(input())
digits = 0
total = 0
largest = 0
smallest = 9
even = 0
odd = 0

for i in range(len(str(n))):
    digit = n % 10
    digits = digits + 1
    total = total + digit

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    n = n // 10

print("Digits:", digits)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even)
print("Odd Digits:", odd)


#Question -69 ------------

s = input()
total_chars = 0
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index = 0

for i in range(len(s)):
    char = s[i]
    total_chars = total_chars + 1

    if i % 2 == 0:
        even_index = even_index + 1

    if char != " ":
        if char.lower() in "aeiou":
            vowels = vowels + 1
        elif char.isalpha():
            consonants = consonants + 1

        if char.isupper():
            uppercase = uppercase + 1
        elif char.islower():
            lowercase = lowercase + 1

print("Total Characters:", total_chars)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Even Index Characters:", even_index)


# Output for Hello World
# Total Characters: 11
# Vowels: 3
# Consonants: 7
# Uppercase: 2
# Lowercase: 8
# Even Index Characters: 6
