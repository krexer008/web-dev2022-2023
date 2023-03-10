n = int(input())


def MinDivisor(x):
    i = 2
    kor = x ** 0.5
    while i <= kor:
        if x % i == 0:
            return i
        i += 1
    return x


print(MinDivisor(n))
