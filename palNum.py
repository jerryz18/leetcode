class Solution(object):
    def isPalindrome(self, x):
        if int(x) < 0:
            return False 
        num = str(x)
        
        for i in range(len(num) / 2):
            if (num[i] == num[len(num) - 1 - i]):
                continue
            else:
                return False
        return True
