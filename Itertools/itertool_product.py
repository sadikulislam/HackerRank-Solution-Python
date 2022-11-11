import itertools
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result  = tuple(itertools.product(A, B))

for item in result:
    print(item, end="")
print("")
