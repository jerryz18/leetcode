class Solution:
    def isPalindrome(self, s: str) -> bool:       
        phrase = ''
        for char in s:
            if char.isalnum():
                phrase += char.lower()
                
        while len(phrase) != 0 or len(phrase) != 1: 
            if len(phrase) == 0:
                break
            if phrase[0] != phrase[-1]:
                return False
            else:
                phrase = phrase[1:-1]
                
        return True
        
