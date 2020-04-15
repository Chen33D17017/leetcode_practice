
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = [1] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                rst[i] = 1
            else:
                rst[i] = rst[i-1] * nums[i-1]
        tmp = 1
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if i != 0:
                rst[j] = rst[j] * tmp
            tmp *= nums[j]
        return rst

def test():
    test_input = [1, 2, 3, 4]
    solution = Solution()
    rst = solution.productExceptSelf(test_input)
    print(rst)


if __name__ == '__main__':
    test()