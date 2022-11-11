if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    iteration = int(input())


    for i in range(iteration):
        command, *number = input().split()
        command = command.lower()

        if command == 'remove':
            s.remove(int(number[0]))

        elif command == 'discard':
            s.discard(int(number[0]))
        
        elif command == 'pop':
            s.pop()

    print(sum(s))