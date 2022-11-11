from itertools import groupby
import re

s = input()

result = [(len(list(g)), int(k)) for k, g in groupby(s)]

for item in result:
    print(item, end=" ")