'''Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

list_a = [i for i in range(999, 99, -1)]

palin_num = 0

for i in range(999, 99, -1):
    for j in list_a:
        check_num = i * j
        string_num = str(check_num)
        if string_num[0] == string_num [-1] and string_num[1] == string_num[-2] and string_num[2] == string_num[-3]:
            if palin_num < check_num:
                palin_num = check_num

print(palin_num)

