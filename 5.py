coffee = ["Dark coffee" , "milk coffee", "hot coffee" , "black coffee", "lava coffee"]
print(coffee.append("green coffee"))
print(coffee) 

coffee.insert(1 , "cold coffeee")
print(coffee)

coffee.pop(2)
print(coffee)
#2
number = [ 1,28,9,6]
print(sorted(number))

number.reverse()
print(number)
print(number.index(28))
#test
cumber = [3, 6, 7,2 ,4,5,8 ]
largest = cumber[0]
for num in cumber:
    if num > largest:
         largest = num
print("The largest number is: ",largest)

nums = [4, 7, 2, 7, 9, 2, 7]
print(nums.count(7))

nums = [4, 7, 2, 7, 9, 2, 7]
count = 0
for num in nums:
     if num == 7:
          count += 1
print(count)

nums.reverse()
print(nums)
     