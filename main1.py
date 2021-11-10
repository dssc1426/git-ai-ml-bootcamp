import math
number = int(input("Enter the Number"))
root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print( "%d is a perfect squ",number)
else:
    print("%d is a perfect square",number)