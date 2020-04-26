class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) and len(text2):
            return 0

        text1 = " " + text1
        text2 = " " + text2
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                print(i, j)
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text1)-1][len(text2)-1]

def main():
    text1 = "abcde"
    text2 = "ace"
    solution = Solution()
    print(solution.longestCommonSubsequence(text1, text2))

def test():
    x, y = 5, 3
    mem = [[0 for _ in range(y)] for _ in range(x)]
    mem[2][2] = 1
    print(mem)


if __name__ == '__main__':
    main()
    # test()