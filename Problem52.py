"""Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


numsearch = True
num_to_check = 1

def numcheck(listnumber, checklist):
    samedigits = True
    for i in checklist:
        if i not in listnumber:
            samedigits = False
        else:
            listnumber.remove(i)
    return samedigits

while numsearch:
    listnum = [int(x) for x in str(num_to_check)]
    num2 = 2 * num_to_check
    list2 = [int(x) for x in str(num2)]
    if numcheck(listnum, list2):
        print('2match on ', num_to_check)
        num3 = 3 * num_to_check
        list3 = [int(x) for x in str(num3)]
        if numcheck(listnum, list3):
            print('3match on ', num_to_check)
            num4 = 4 * num_to_check
            list4 = [int(x) for x in str(num4)]
            if numcheck(listnum, list4):
                print('4match on ', num_to_check)
                num5 = 5 * num_to_check
                list5 = [int(x) for x in str(num5)]
                if numcheck(listnum, list5):
                    print('5match on ', num_to_check)
                    num6 = 6 * num_to_check
                    list6 = [int(x) for x in str(num6)]
                    if numcheck(listnum, list6):
                        numsearch = False
                        print(num_to_check)
    num_to_check += 1
