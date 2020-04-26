class Solution:
    def sortedSquares(self, A):
        if len(A) == 0 or A == None:
            return []
        rst = [0] * len(A)
        l, r = 0, len(A)-1
        p = len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                rst[p] = A[l] ** 2
                l += 1
            else:
                rst[p] = A[r] ** 2
                r -= 1
            p -= 1
        return rst

def main():
    test = [-4,-1,0,3,10]
    test2 = [-7, -3, 2, 3, 11]
    solution = Solution()
    print(solution.sortedSquares(test))
if __name__ == '__main__':
    main()