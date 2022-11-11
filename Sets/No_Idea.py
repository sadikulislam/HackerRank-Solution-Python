from re import I


if __name__ == '__main__':
    n = input().split()
    items = list(map(int, input().split()))

    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    count = 0
    for i in items:
        if i in A:
            count += 1
        elif i in B and i not in A:
            count -= 1

    print(count)