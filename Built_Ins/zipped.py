n, x = map(int, input().split())
s = []

for i in range(x):
    k = list(map(float, input().split()))
    s.append(k)

z = zip(*s)
for i in z:
    res = sum(i) / len(i)
    print(res)