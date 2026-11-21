class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        else:
            cnt1 = Counter(s)
            cnt2 = Counter(t)

            if (cnt1 == cnt2):
                return True
            else:
                return False
            




        
        



s = "racecar"
t = "carrace"

solution = Solution()

print(solution.isAnagram(s,t))
