'''Problem 6
Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.
'''

squares = [i **2 for i in range(1,101)]

print(squares)

squaretotal = 0

for i in squares:
    squaretotal += i

sumtotal = 0
for i in range(1,101):
    sumtotal += i

sq_sumtotal = sumtotal ** 2

print(sq_sumtotal)
print(squaretotal)
print(sq_sumtotal - squaretotal)