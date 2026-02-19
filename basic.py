print("Keerthana.k , ECE,  8.5 ")

age = int(input("Enter your age:  "))
after = age + 5
print("After five years the will be: ",after )

a = 10
b = 5
print("sum: ", a+b)
print("difference: ",a-b)
print("product: ", a*b)
print("division: ",a/b)

a = 10
print("Square: ",a**2)
print("Cube: ",a**3)

a = int(input("Enter a number: "))
if a%2 == 0:
  print("Even")
else:
  print("Odd")


a = int(input("Enter first number:"))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a>=b) and (a>=c):
  largest = a
elif(b>=a) and (b>=c):
  largest = b
else:
   largest = c
print("Largest number is: ",largest)

a = int(input("Enter a number: "))
if a > 0:
  print("Positive umber")
elif a<0:
  print("Negative number")
else:
  print("Zero")
  print("Entered number is: ", a)

cel = float(input("Enter a celsius: "))
fahr = (cel*9/5)+32
print("fahrenheit degree is: ",fahr) 





    