from itertools import permutations

S, k = input().split()

result = sorted(list(permutations(S, int(k))))

for item in result:
    print(*item, sep='')
