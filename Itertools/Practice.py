import itertools
import operator
import re

"""accumulate()"""

#data = [1 , 2, 3, 4, 5]

# result = itertools.accumulate(data, operator.mul)

# for i in result:
#     print(i)

# result = itertools.accumulate(data, max)
# for i in result:
#     print(i)

"""Combinations()"""

# shapes = ['circle', 'triangle', 'square',]
# result = itertools.combinations(shapes, 2)
# for i in result:
#     print(i)

"""combinations_with_replacement()"""
# shapes = ['circle', 'triangle', 'square',]

# result = itertools.combinations_with_replacement(shapes, 2)

# for i in result:
#     print(i)

"""Count()"""

# for i in itertools.count(0, 5):
#     print(i)
#     if i > 20:
#         break

"""Cycle"""
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
# for color in itertools.cycle(colors):
#     print(color)

"""Chain()"""
name = ["sadik", "Mahadi"]
number = [1, 2, 3]
go = {1: "sadik", 2:"rahil", 3:"John"}

result = itertools.chain(number, name, go)
for each in result:
         #if each == 'John':
            print(each)

"""dropwhile"""

# data = [11, 2, 3, 10, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# result = itertools.filterfalse(lambda x: x<7, data)
# for each in result:
#     print(each)


# Matrix = [[2, 1, 5],
#           [5, 99, 0],
#           [33, 2, 4]]
          
# row_max = [max(row) for row in Matrix]
# print(row_max)