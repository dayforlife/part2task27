def myfunc():
    list_ = [1, 2, 3, 4, -5, -6, -7, 8, -9]
    pos = []
    neg = []
    for i in list_:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    print(pos, neg)
myfunc()