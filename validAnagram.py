class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            if s[i] not in countS:
                countS[s[i]] = 1
            else:
                countS[s[i]] += 1
                
            if t[i] not in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1
                
        for c in countS:
            if countS[c] != countT.get(c):
                return False
        
        return True
