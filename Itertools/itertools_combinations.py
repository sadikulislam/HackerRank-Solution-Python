from itertools import combinations

S, k = input().split()

for i in range(1, int(k)+1):
    result = list(combinations(sorted(S), i)) 
    for item in result:
        print(*item, sep='')