# 49. Group Anagrams


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0 or strs == None:
            return []
        rst = {}
        for elem in strs:
            s_elem = "".join(sorted(elem))
            if s_elem not in rst:
                rst[s_elem] = [elem]
            else:
                rst[s_elem].append(elem)
        return [v for k, v in rst.items()]





def main():
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(test_input))

if __name__ == '__main__':
    main()