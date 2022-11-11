import re
t = int(input())
for i in range(t):
    s = input()
    if re.match(r"^[+-]?[0-9]*\.[0-9]+$", s):
        print(True)
    else:
        print(False)