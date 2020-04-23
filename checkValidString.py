class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == '*':
                lo -= 1
                hi += 1
            else:
                lo -= 1
                hi -= 1
            if hi < 0:
                return False
        return lo <= 0

    def test(self, s):
        lo = hi = 0
        for c in s:
            print(c)
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            print(lo, hi)
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0

def test():
    # **((*
    test_input = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    test_input = "()"
    solution = Solution()
    # print(solution.checkValidString(test_input))
    solution.test(test_input)

if __name__ == '__main__':
    test()