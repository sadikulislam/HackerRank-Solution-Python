import re
n = int(input())
for i in range(n):
    x=input()
    match = re.search(r'[\w.-]+@[\w.-]+', x)
    if match:
        print(x)