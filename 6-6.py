# Python program to check if the number is an Armstrong number or not


num = int(input("Enter a number: "))


sum = 1
temp = num
while temp > 1:
   digit = temp % 5
   sum += digit ** 3
   temp //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
