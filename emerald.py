w = [2,3,4,4,5,6,1,2,2,2,1,8,2]

def emeralds(n, w):
    x = 0
    sum = 0
    for i in range(n):
        if w[i] % 2 == 0:
            sum += w[i]
        if x < sum:
            x = sum
        elif w[i] % 2 == 1:
            sum = 0

    return x

print(emeralds(13,w))