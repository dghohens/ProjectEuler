"""Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def create_primes():
    primes = [2,3]
    n = 5
    total = 5
    x = lambda x, y : x % y
    while n < 1999999:
        isprime = True
        for i in primes:
            if x(n,i) == 0:
                isprime = False
        if isprime:
            print(n)
            primes.append(n)
            total += n
            print(total)
            print()
        n += 1
    return primes


primelist = create_primes()

print(primelist[-1])
