if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    operation = int(input())

    for _ in range(operation):
        command, *m = input().split()
        b = set(map(int, input().split()))

        if command == 'update':
            a.update(b)

        elif command == 'intersection_update':
            a.intersection_update(b)
            
        elif command == 'difference_update':
            a.difference_update(b)

        elif command == 'symmetric_difference_update':
            a.symmetric_difference_update(b)
        
    print(sum(a))