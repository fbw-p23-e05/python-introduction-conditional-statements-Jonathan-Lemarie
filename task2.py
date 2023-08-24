
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

difference = abs(num1 - num2)

if num1 > num2:
     result = difference * 2
else:
    result = difference
print("The result of calculation is", result)