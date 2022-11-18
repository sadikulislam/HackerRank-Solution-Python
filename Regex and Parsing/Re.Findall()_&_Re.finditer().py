import re

s = input()
matche= re.findall(r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*)([AEIOUaeiou]{2,})([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',s)

if len(matche) > 0:
    for match in matche:
        print(match[1])
else:
    print(-1)