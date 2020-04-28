class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or not matrix:
            return 0
        rst = 0
        dp = [[ 0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    rst = max(rst, dp[i][j]**2)
        return rst



def main():
    test_pattern = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    solution = Solution()
    print(solution.maximalSquare(test_pattern))

if __name__ == '__main__':
    main()