'''Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

square_root = int(sqrt(600851475143))

possible_list = [i for i in range(3, square_root + 1, 2)]

class create_sieve:
    def __init__(self, inlist, sievenum, endnum):
        self.inlist = inlist
        self.sievenum = sievenum
        self.endnum = endnum

    def extend_sieve(self):
        for i in range(self.sievenum, self.endnum, 2 * self.sievenum):
            if i not in self.inlist:
                self.inlist.append(i)
        return self.inlist


def find_primes(in_list):
    prime_list = [2, 3]
    x = create_sieve(prime_list, 3, square_root)
    composite_list = x.extend_sieve()
    for i in possible_list:
        if i in composite_list:
            pass
        else:
            prime_list.append(i)
            print(i)
            x = create_sieve(composite_list, i, square_root)
            composite_list.append(x.extend_sieve)
            print(composite_list)



primes = find_primes(possible_list)
print(primes)