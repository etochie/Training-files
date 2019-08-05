def deliteli(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    return sum(l)


def get_friendlys(n):
    res = []
    for j in range(1, n):
        if j not in res:
            tmp = deliteli(j)
            if j == deliteli(tmp) and j != tmp:
                res.append(j)
                res.append(tmp)
    return res


