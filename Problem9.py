"""Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a_list = [i for i in range(1, 1001)]
b_list = [i for i in range(333, 1001)]
c_list = [i for i in range(334, 1001)]

x = lambda a,b,c: a * b * c

for c in c_list:
    for b in b_list:
        for a in a_list:
            if a + b + c == 1000:
                if (a**2 + b**2) == c**2:
                    print(x(a,b,c))