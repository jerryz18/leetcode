class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        newDigits = [1]
        
        digits[-1] += 1
        
        for i in range(len(digits) - 1, -1, -1):
            if carry == True:
                digits[i] += 1
                carry = False
                
            if digits[i] >= 10:
                digits[i] %= 10
                carry = True
        
        if carry == True:
            return newDigits + digits
        
        return digits
