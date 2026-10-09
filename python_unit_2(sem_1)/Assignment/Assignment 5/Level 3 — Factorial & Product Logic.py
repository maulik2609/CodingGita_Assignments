#Question-15 -------------------------

n = int(input("Enter Number :"))
fatorial = 1
for i in range(1,n+1):
    factorial = factorial*i
print(factorial)


#Question-16 -------------------------

n = int(input("Enter Number :"))
product = 1
for i in range(1,n+1):
    product = product*i
    print(str(i)+"!=", product )

#Question-17 -------------------------

n = int(input("Enter Number :"))
product = 1
for i in range(1,n+1):
    if i%2==0:
        product = product*i
print(product)

#Question-18 -----------------------

n = int(input("Enter Number : "))
product = 1
for i in range(1,n+1):
    if i%2!=0:
        product = product*i
print(product)

#Question-19 ---------------

n = int(input())
result = 1

for i in range(n, 0, -2):
    result = result * i

print(result)

#Question-20 ---------------

n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + i * i

print(total)

#Question-21 ----------------

n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + i * i * i

print(total)

#Question-22 ------------------

n = int(input())
fact = 1
total = 0

for i in range(1, n + 1):
    fact = fact * i
    total = total + fact

print(total)







