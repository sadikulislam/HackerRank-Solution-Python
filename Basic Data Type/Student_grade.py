if __name__ == '__main__':

    students = []
    grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
        grade.append(score)

    x = sorted(set(grade))
    student_name = []

    for i in students:
        if x[1] == i[1]:
            student_name.append(i[0])

    student_name.sort()

    for i in student_name:
        print(i)