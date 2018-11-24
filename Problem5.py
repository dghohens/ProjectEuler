'''Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
Find the smallest positive number that is evenly divisible by all the numbers from 1 to 20.
'''

# 20 = 2 * 2 * 5
# 19 is prime
# 18 = 2 * 3 * 3
# 17 is prime
# 16 = 2 * 2 * 2 * 2
# 15 = 3 * 5
# etc, etc

print(20 * 19 * 9 * 17 * 4 * 7 * 13 * 11)