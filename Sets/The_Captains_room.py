
from collections import Counter
from re import I


if __name__ == '__main__':

    n = int(input())
    rooms = list(map(int, input().split()))
    new = set(rooms)
    count = Counter(rooms)

    for i in new:
        if count[i] == 1:
            print(count.most_common(-1)[0])