## 53. Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums == None:
            return 0
        tmp, rst = 0, 0
        for num in nums:
            tmp = num if tmp < 0 else tmp + num
            rst = max(rst, tmp)
        return rst

def main():
    test_input = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(test_input))

if __name__ == '__main__':
    main()