

def build(string):
    n = len(string)
    rst = [0] * n
    pre_flag = False
    i, j = 0, 1
    # loop to the end
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
    # Add -1 to first elems
    rst.insert(0, -1)
    rst.pop()
    return rst

def KMP_find(src, target):
    pre = build(target)
    # i in src, j in target
    i, j = 0, 0
    p = []
    while i < len(src):
        # move i & j until src[i] != target[j] or all char match
        while j < len(target) and src[i] == target[j]:
            i+= 1
            j+= 1

        # The case when match
        if j == len(target):
            p.append(i - j)
            j -= 1

        # The case when unmatch
        # Even the first char is not match
        if pre[j] == -1:
            i += 1
            j = 0
        # Not all char match
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
