def condition(n):
    if n % 2 == 0 and n >= 2 and n <= 5:
        return "Not Weird"
    
    elif n % 2 == 0 and n >= 6 and n <= 20:
        return "Weird"
    
    elif n % 2 == 0 and n >= 5:
        return "Not Weird"
    
    else:
        return "Weird"
        

if __name__ == '__main__':
    n = int(input().strip())
    
    result = condition(n)
    print(result)