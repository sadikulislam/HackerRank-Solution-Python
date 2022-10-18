#str = "Sadik"
#list = [1, 5, 7, 9, 2]
#tup = (1, 5, 8, 9)
list = {1:"sadik", 2:'Rahim', 3:"Mahadi"}

res = [list[i] for i in list if i % 2 != 0]
print(res)