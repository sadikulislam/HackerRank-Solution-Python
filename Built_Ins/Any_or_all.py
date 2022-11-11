n = int(input())
l = list(map(int, input().split(" ")))
print(any([str(item) == str(item)[::-1] for item in l]) and all([int(item) >= 0 for item in l]))

# n = int(input())

# lst = input().split()[:n]

# print( any(i == i[::-1] for i in lst) and all(int(i) >= 0 for i in lst) )