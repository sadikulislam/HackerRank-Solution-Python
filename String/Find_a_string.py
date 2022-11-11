def count_substring(string, sub_string):
    count = 0
    l = len(string)
    for i in range(0, l):
        if string[i:l].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)