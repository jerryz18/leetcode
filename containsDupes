class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        
        for num in nums:
            if num not in appeared:
                appeared[num] = 1
            else:
                return True
        return False
