#Question-7 -----------------

st= input("Enter Start Number :")
end = int(input("Enter End Number :"))
sum = 0
for i in range(st,end+1):
    sum = sum + i
print(sum) 

#Question-8 --------------------

n = int(input("Enter Number :"))
count = 0
for i in range(1,n+1):
    if i%3==0:
        count = count+1
print(count)


#Question-9 --------------------

n = int(input("Enter Number :"))
sum = 0
for i in range(1,n+1):
    if i%4==0:
        sum = sum+i
print(sum)

#Question-10 --------------------

n = int(input("Enter Number :"))
count = 0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        count = count+1
print(count)


#Question-11 ----------------------

n = int(input("Enter Number :"))
sum = 0
for i in range(1,n+1):
    if i%3!=0:
        sum = sum+i
print(sum)

#Question-12 -----------------------

N = int(input("Enter Number :"))

even = 0
odd = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even, ", Odd =", odd)

#Question-13 -----------------------

n = int(input("Enter Number :"))
sum = 0
for i in range(1,n+1):
    sum = sum+i
    print(sum)


#Question-14 ------------------------

n = int(input("Enter Number :"))
product = 1
for i in range(1,n+1):
    product = product*i
    print(product)
