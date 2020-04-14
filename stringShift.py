
class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        for direction, amount in shift:
            if direction:
                s = s[-amount:] + s[:-amount]
            else:
                s = s[amount:]+ s[:amount]
            print(s)
        return s

def test():
    # shift = [[1,1],[1,1],[0,2],[1,3]]
    # s = "abcdefg"
    s = "joiazl"
    shift = [[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]
    solution = Solution()
    solution.stringShift(s, shift)

if __name__ == '__main__':
    test()