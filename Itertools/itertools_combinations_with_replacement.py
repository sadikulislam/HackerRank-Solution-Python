from itertools import combinations_with_replacement

S, k = input().split()

result =list(combinations_with_replacement(sorted(S), int(k)))

for item in result:
    print(*item, sep='')