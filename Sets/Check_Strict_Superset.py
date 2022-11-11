if __name__ == '__main__':
    a = set(map(int, input().split()))
    n = int(input())

    res = []
    for i in range(n):
        s = set(map(int, input().split()))

        if s.issubset(a):
            res.append(True)
        else:
            res.append(False)

    if False in res:
        print(False)
    else:
        print(True)