def calc(a):
    mydict = {}
    for every in range(1, 10):
        count = 0
        for each in a:
            if each % every == 0:
                count += 1
            mydict[every] = count

    return mydict


print(calc([0,1,2,8,9,12,46,76,82,15,20,30]))