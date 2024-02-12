def mysort(mylist):
    lena = len(mylist)
    for x in range(0,lena):
        minindex = x
        for y in range(x,lena):
            if (mylist[y] < mylist[minindex]):
                minindex = y
        tmp = mylist[x]
        mylist[x] = mylist[minindex]
        mylist[minindex] = tmp
    return(mylist)
a = [7, 1, 2, 8, 5, 19, 3, 14, 15]
print(mysort(a))
