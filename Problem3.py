'''Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

square_root = int(sqrt(600851475143))

possible_list = [i for i in range(3, square_root + 1, 2)]

def find_primes(in_list):
    prime_list = []
    is_divisible = True
    x = lambda a, b: a % b == 0
    for i in in_list:
        for j in in_list[:in_list.index(i)]:
            is_divisible = x(i,j)
            if is_divisible == True:
                print(i)
                print(j)
                print()
                break
        if is_divisible == False:
            prime_list.append(i)
    return prime_list


primes = find_primes(possible_list)
print(primes)