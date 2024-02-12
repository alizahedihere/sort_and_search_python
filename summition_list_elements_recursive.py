def summition(li):
    if len(li) == 1:
        return li[0]
    return li[-1] + summition(li[:-1])
a = [1 ,2 ,3 ,4 ,5]
print(summition(a))
