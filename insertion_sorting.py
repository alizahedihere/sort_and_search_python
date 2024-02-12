def mysort(mylist):
    lenmylist = len(mylist)
    for x in range(0, lenmylist):
        for y in range(x, 0, -1):
            if (mylist[y] < mylist[y-1]):
                tmp = mylist[y-1]
                mylist[y-1] = mylist[y]
                mylist[y] = tmp
    return mylist
a = [3, 1, 4, 9, 2, 6, 3, 2, 89, 43, 12]
resault = mysort(a)
print(resault)
