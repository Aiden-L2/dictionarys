def emeralds(n, w):
    i = 0
    x = 0
    n = 0
    sum = 0
    sum += w[i]
    for e in emeralds(n):
        if sum % 2 == 0:
            i += 1
            if sum > x:
                sum = x
            elif sum % 2 == 1:
                sum = 0
                i += 1
    emeralds(13,[2,3,4,4,5,6,1,2,2,2,1,8,2])
    print(emeralds)



"""     w = [2,3,4,4,5,6,1,2,2,2,1,8,2] """