n = int(input())


def IsPrime(x):
    i = 2
    kor = x ** 0.5
    while i <= kor:
        if x % i == 0:
            return False
        i += 1
    return True


if IsPrime(n):
    print('YES')
else:
    print('NO')
