def list_comp(x, y, z, n):
    """ Using mulitple Loops """
    list = []
    
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    list.append([i, j , k])

    return list


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = list_comp(x, y, z, n)
    print(result)
