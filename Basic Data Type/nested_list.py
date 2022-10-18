if __name__ == '__main__':

    students_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students_list.append([name, score])

    second_lowest_score = sorted({x[1] for x in students_list})
    name = []

    for i in students_list:
        if second_lowest_score[1] == i[1]:
            name.append(i[0])

    name.sort()
    for i in name:
        print(i)