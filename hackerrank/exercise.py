def count_substring(string, sub_string):
    s=0
    for i in range(len(string)):
        c=0
        if sub_string[0]==string[i]:
            for j in range(len(sub_string)):
                if i<len(string) and sub_string[j]==string[i]:
                    i=i+1
                    c=1
                else:
                    c=0
        if c:
            s=s+1
    return s
    
                



if __name__ == '__main__':
    string = "ababcab"
    sub_string = "ab"
    
    count = count_substring(string, sub_string)
    print(count)