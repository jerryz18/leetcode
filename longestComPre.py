class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            temp = prefix
            minimum = len(prefix)
            if minimum > len(strs[i]):
                minimum = len(strs[i])
            for j in range(minimum):
                if prefix[j] != strs[i][j]:
                    if j == 0:
                        return ""
                    prefix = prefix[0:j]
                    break
            if temp == prefix and len(prefix) > minimum:
                prefix = prefix[0:minimum]
            
        return prefix
        
