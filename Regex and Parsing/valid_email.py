import re
import email.utils

n = int(input())

for i in range(n):
    x = email.utils.parseaddr(input())
    match = re.match(r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-z]{1,3}$', x[1])

    if match:
        print(email.utils.formataddr(x))