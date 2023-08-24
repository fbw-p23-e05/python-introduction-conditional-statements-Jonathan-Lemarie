
total_amount = 0

for i in range(3):
    num = int(input('enter number: '))
    total_amount += num

if total_amount / 3 == num:
    print('The triple sum is:', total_amount*3)
else:
    print(' the sum is: ' , total_amount)