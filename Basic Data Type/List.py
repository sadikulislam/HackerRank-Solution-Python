if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command, *number = input().split()
        command = command.lower()

        if command == 'insert':
            arr.insert(int(number[0]), int(number[1]))

        elif command == 'print':
            print(arr)

        elif command == 'remove':
            arr.remove(int(number[0]))

        elif command == 'append':
            arr.append(int(number[0]))
        
        elif command == 'sort':
            arr.sort()
        
        elif command == 'pop':
            arr.pop()
        
        elif command == 'reverse':
            arr.reverse()
        
        else:
            print("Wrong command, Please enter right command.")