'''Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def create_primes():
    primes = [2,3]
    n = 5
    x = lambda x, y : x % y
    while len(primes) < 10002:
        isprime = True
        for i in primes:
            if x(n,i) == 0:
                isprime = False
        if isprime:
            print(n)
            primes.append(n)
        n += 1
    return primes

prime_nums = create_primes()

print('\n')
print(prime_nums[10000])
