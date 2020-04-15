class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        def helper(l, r, elems):
            if l == 0 and r == 0:
                self.ans.append(elems)
            if l != 0:
                helper(l-1, r+1, elems + '(')
            if r != 0:
                helper(l, r-1, elems + ')')
        helper(n, 0, "")
        return self.ans

def test():
    test_input = 3
    solution = Solution()
    rst = solution.generateParenthesis(test_input)
    print(rst)


if __name__ == '__main__':
    test()