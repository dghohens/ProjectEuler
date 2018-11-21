'''Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# I'm practicing classes here, so that's why this is way overcomplicated.

class IsThree:
    def __init__(self, in_number, isdivisible = False):
        self.in_number = in_number
        self.isdivisible = isdivisible

    def mult3(self):
        if self.in_number % 3 == 0:
            self.isdivisible = True
        return self.isdivisible


class IsFive:
    def __init__(self, in_number, isdivisible = False):
        self.in_number = in_number
        self.isdivisible = isdivisible

    def mult5(self):
        if self.in_number % 5 == 0:
            self.isdivisible = True
        return self.isdivisible

total = 0

for i in range(1000):
    x = IsThree(i)
    y = IsFive(i)
    if x.mult3() == True or y.mult5() == True:
        total += i

print(total)