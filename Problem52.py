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
    list2 = [2 * x for x in listnum]
    if numcheck(listnum, list2):
        list3 = [3 * x for x in listnum]
        if numcheck(listnum, list3):
            list4 = [4 * x for x in listnum]
            if numcheck(listnum, list4):
                list5 = [5 * x for x in listnum]
                if numcheck(listnum, list5):
                    list6 = [6 * x for x in listnum]
                    if numcheck(listnum, list6):
                        numsearch = False
                        print(num_to_check)
    num_to_check += 1
