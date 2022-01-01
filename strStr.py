class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        length = len(needle)
        for i in range (len(haystack)):
            if haystack[i] == needle[0]:
                temp = haystack[i:i+length]
                if temp == needle:
                    return i    
        return -1
