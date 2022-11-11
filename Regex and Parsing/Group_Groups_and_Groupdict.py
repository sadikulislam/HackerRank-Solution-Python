import re 
res = re.findall(r"([a-zA-Z0-9])\1+",input()) 
if res: 
    print(res[0]) 
else: 
    print(-1)