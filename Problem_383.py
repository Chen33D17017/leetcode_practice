class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mem = {}
        for s in magazine:
            if s not in mem:
                mem[s] = 1
            else:
                mem[s] += 1
        
        for r in ransomNote:
            if r not in mem or mem[r] < 1:
                return False
            else:
                mem[r] -= 1
        return True
    
def main():
    a = "aa"
    b = "aab"
    solution = Solution()
    print(solution.canConstruct(a, b))
    

if __name__ == "__main__":
    main()