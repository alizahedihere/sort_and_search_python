def mysort(mylist):
    lenmylist = len(mylist)
    for x in range(0, lenmylist):
        for y in range(0, lenmylist-1):
            if (mylist[y] > mylist[y+1]):
                tmp = mylist[y+1]
                mylist[y+1] = mylist[y]
                mylist[y] = tmp
    return mylist
a = [4, 3, 2, 1, 0]
resault = mysort(a)
print(resault)
