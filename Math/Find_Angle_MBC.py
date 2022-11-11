from math import degrees
from math import atan2

ab = float(input())
bc = float(input())

ans = round(degrees(atan2(ab,bc)))
print(str(ans) + chr(176))