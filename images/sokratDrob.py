def ReduceFraction(p, q):
    i = int(q % p)
    if i == 0:
        q = m // p
        p = n // p
        return p, q
    else:
        ReduceFraction(i, p)


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
