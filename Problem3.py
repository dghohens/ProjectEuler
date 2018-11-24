'''Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

num_to_find = 600851475143

# square_root = int(sqrt(num_to_find))


def make_primes(max_num):
    primes = [2, 3]
    for j in range(25, max_num, 24):
        root = sqrt(j)
        if root == int(root):
            is_prime = True
            for i in primes:
                if int(root) % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(int(root))
                if max_num % int(root) == 0:
                    print(int(root))
                    print(max_num)
                    if max_num // int(root) == 0:
                        print()
                        print(int(root))
                        print()
                        break
                    else:
                        max_num = max_num // int(root)
    return primes


print(make_primes(num_to_find))

'''
class factor_checker:
    def __init__(self, primelist, numcheck):
        self.primelist = primelist
        self.numcheck = numcheck

    def find_factors(self):
        highestnum = 0
        for i in self.primelist:
            if numcheck % i == 0:
                highestnum = i
        return highestnum


prime_list = make_primes(num_to_find)

x = factor_checker(prime_list, num_to_find)

print(x.find_factors())

'''