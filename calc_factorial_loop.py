def fact(a):
    resalt = 1
    for x in range(a,1,-1):
        resalt *= x
    return resalt
print(fact(3))
