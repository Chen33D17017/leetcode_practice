

def build(string):
    n = len(string)
    rst = [0] * n
    pre_flag = False
    i, j = 0, 1
    while j < n:
        if string[i] != string[j]:
            if not pre_flag:
                rst[j] = i
            else:
                rst[j] = rst[i-1]
                pre_flag = False
                i = 0
        else:
            i += 1
            rst[j] = i
            pre_flag = True
        j += 1
    rst.insert(0, -1)
    rst.pop()
    return rst

def KMP_find(src, target):
    pre = build(target)
    i, j = 0, 0
    p = []
    while i < len(src):
        while j < len(target) and src[i] == target[j]:
            i+= 1
            j+= 1

        if j == len(target):
            p.append(i - j)
            j -= 1

        if pre[j] == -1:
            i += 1
            j = 0
        else:
            j = pre[j]
    return p



if __name__ == '__main__':

    src2 = "ABAACABABCAC"
    check = "ABABC"
    test = "dsgwadsgz"
    src = "adsgwadsxdsgwadsgz"
    print(KMP_find(src2, check))
    print(src2[5:5+len(check)])
    # build(test)
