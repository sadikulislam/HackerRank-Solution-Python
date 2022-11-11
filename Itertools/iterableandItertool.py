from itertools import combinations, filterfalse

n = int(input())
s = input().split()
#s = input().split(" ", n)
#s = input().replace(" ", "")
k = int(input())

combs = list(combinations(s, k))
new_combs = list(filterfalse(lambda x: 'a' not in x, combs))

result = len(new_combs) / len(combs)

print(result)
