"""Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def create_primes():
    primes = [2]
    total = 2
    for possiblePrime in range(3, 2000001, 2):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
            total += possiblePrime
            print(total)

    return (primes)


primelist = create_primes()
