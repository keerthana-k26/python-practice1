numbers = [3, 7, 2, 9, 4]
total = 0
for n in numbers:
    total = total + n
print("Sum: ",total)

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest: ", largest)

count = 0
for n in numbers:
    if n % 2 == 0:
        count = count + 1
print("Even count: ",count)

even_numbers = []
for n in numbers:
    if n % 2 ==0:
        even_numbers.append(n)
print("Even numbers: ",even_numbers)