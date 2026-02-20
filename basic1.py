n = int(input("Enter a number: "))
for i in range (1 , n +1):
    print(i)

n = int(input("Enter a number: "))
for i in range(n , 0 , -1):
    print(i)

n = int(input("Enter a number: "))
for i in range(n , 0 , -1):
    if i % 2 != 0:
        print(i)

n = int(input("Enter a number: "))
for i in range( 1, n+1):
    if i % 2 == 0:
        print(i)

n = int(input("Enter a number: "))
sum = int((n *(n + 1))/2)
print("Sum of first n numbers: ", sum)

n = int(input("Enter a nuber: "))
factorial = 1
if n < 0:
    print("factorial is not provided for negative numbers")
else: 
    for i in range(1 , n+1):
        factorial = factorial * i
        print("Factorial is : ",factorial)



