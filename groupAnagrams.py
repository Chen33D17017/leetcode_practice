
class Solution:
    def groupAnagrams(self, strs):
        tmp = {}
        for val in strs:
            sorted_val = "".join(sorted(val))
            if sorted_val in tmp:
                tmp[sorted_val].append(val)
            else:
                tmp[sorted_val] = [val]
        rst = [val for _, val in tmp.items()]
        return rst



def test():
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    solution.groupAnagrams(test_input)

if __name__ == '__main__':
    test()