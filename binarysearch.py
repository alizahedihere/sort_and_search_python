def binarysearch(li, x):
    print(li)
    if len(li) == 1:
        return li[0] == x
    middle = len(li)//2
    if li[middle] == x:
        return True
    if x>li[middle] and middle > 0:
        return binarysearch(li[-middle:],x)
    else:
        return binarysearch(li[0:middle],x)
a = [1,2,3,4,5,6,7]
print(binarysearch(a,2))
