

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # check whether if the zero can by passed
        tmp = 0
        for i, num in enumerate(nums):
            if num == 0:
                if tmp <= i and i < len(nums)-1:
                    return False
            tmp = max(tmp, num + i)
        return True


def main():
    test = [3, 2, 1, 0, 4]
    # test = [2, 0, 0]
    solution = Solution()
    ans = solution.canJump(test)
    print(ans)

if __name__ == '__main__':
    main()