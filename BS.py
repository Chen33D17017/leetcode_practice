

def find_cross(test):
    left ,right = 0, len(test)-1
    while right -1 != left:
        mid = (right + left) // 2
        if test[mid] == test[right]:
            right = mid
        else:
            left = mid
    print(right)


def main():
    test = [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0]
    test = sorted(test)
    print(test)
    find_cross(test)



if __name__ == '__main__':
    main()