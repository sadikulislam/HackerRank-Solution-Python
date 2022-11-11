import re
n = int(input())
for i in range(n):
    s = re.match(r"^[789][0-9]{9}$", input())
    if s:
        print("YES")
    else:
        print("NO")