
def computeLPS(text):
    length = len(text)
    LPS = [0]*length
    slow = 0
    fast = 1

    while fast<length:
        if text[fast]==text[slow]:
            slow+=1
            LPS[fast] = slow
            fast+=1
        elif text[fast]!=text[slow] and slow>0:
            slow-=1
        else:
            LPS[fast] = 0
            fast+=1

    return LPS

def KMP(text,pattern):
    if text == '' or pattern == '':
        return -1

    LPS = computeLPS(pattern)
    limit = len(pattern)
    j = 0
    flag = 0

    for i in range(len(text)):        
        if text[i] == pattern[j]:
            j+=1
            if j == limit:
                print("pattern found at index " + str(i-limit+1))
                flag = 1
                break

        elif text[i] != pattern[j]:
            j = LPS[j]

    if flag == 0:
        print("pattern not found in string")


if __name__=='__main__':
    #sample test cases
    string = "acfacabacabacacdkacabacacd"
    pattern1 = "acabacacd"
    pattern2 = "abacabacacdk"
    pattern3 = 'fab' 
    

    for pattern in [pattern1,pattern2,pattern3]:
        KMP(string,pattern)



