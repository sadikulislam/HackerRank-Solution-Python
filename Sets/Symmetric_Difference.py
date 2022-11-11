# Enter your code here. Read input from STDIN. Print output to STDOUT
def sys_diff(x,y):
    myset = (x.symmetric_difference(y))
    print(*sorted(myset), sep='\n')

if __name__ == '__main__':
    M = int(input())
    x = set(map(int, input().split()))
    N = int(input())
    y = set(map(int, input().split()))

    sys_diff(x,y)