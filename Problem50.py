"""Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def create_primes():
    primes = [2]
    for possiblePrime in range(3, 1000001, 2):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)

    return (primes)


prime_list = create_primes()

print(prime_list)

print(len(prime_list))

max_num = 0
max_combo = 0
for i in range(5150):
    for j in range(1000):
        total = 0
        for k in prime_list[i:i+j]:
            total += k
            if total > 1000000:
                break
        if total in prime_list and j > max_combo:
            max_combo = j
            max_num = total
            print(i, max_num, max_combo, '\n')

print(max_num)
