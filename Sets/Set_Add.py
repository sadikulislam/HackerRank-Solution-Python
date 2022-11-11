x = int(input())
countries = []

for i in range(x):
    countries.append(input())

print(len(set(countries)))