"""Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having
seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
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


def replace_numbers(number,  primelist):
    '''This function accepts a single number. The function will then check if 00, 11, or 22 fit the pattern.
    If one of those numbers fits the pattern, this function will then check for 7 more matches on this pattern.
    '''
    length = len(str(number))
    for i in range(0, length - 2):
        for j in range(i, length - 1):
            listnum = list(str(number))
            totalprimes = 0
            for k in range(10):
                listnum[i] = str(k)
                listnum[j] = str(k)
                if int(''.join(listnum)) in primelist:
                    totalprimes += 1
                    print(''.join(listnum))
    return totalprimes


prime_list = create_primes()


for i in prime_list[5600:]:
    print('\n', i, '\n')
    if replace_numbers(i, prime_list) >= 8:
        print('Possible hit: ', i)
        break
