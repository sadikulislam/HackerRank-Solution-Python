if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# Using set() method
    # x = sorted(set(arr))
    # print(x[-2])

# # Using list Comprehension
#     res = []
#     [res.append(i) for i in arr if i not in res]
#     x = sorted(res)
#     print(x[-2])

# Using loop 

    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    res = sorted(res)
    print(res[-2])