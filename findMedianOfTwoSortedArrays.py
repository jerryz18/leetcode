class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = sorted(nums1 + nums2)
        length = len(newList)
        
        if length % 2 == 1:
            return float(newList[length//2])
        else:
            return (newList[(length//2) - 1] + newList[length//2])/2.0
