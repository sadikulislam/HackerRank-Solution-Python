import cmath

n = input()
num = (complex(n))
r = abs(num)
phi = cmath.phase(num)

print(r)
print(phi)