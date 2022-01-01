class Solution(object):
    def searchInsert(self, nums, target): 
        length = len(nums)
        half = length//2
        high, low = length - 1, 0
        while True:
            if target > nums[half]:
                low = half + 1
            elif target < nums[half]:
                high = half - 1
            elif nums[half] == target:
                break
            half = (high-low)//2
        return half     
