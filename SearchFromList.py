
class Solution:
    def search(self, nums, target):
        if len(nums) == 0 or nums == None:
            return -1
        left = 0
        right = len(nums) - 1
        while right > left:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        tmp = left
        left = 0
        right = len(nums) - 1
        if target >= nums[tmp] and target <= nums[right]:
            left = tmp
        else:
            right = tmp

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid -1 
        return -1





def test():
    test_input = [1]
    solution = Solution()
    ans = solution.search(test_input, 1)
    print(ans)

if __name__ == '__main__':
    test()