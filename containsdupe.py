class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
                
        for key in d:
            valLength = len(d[key])
            if valLength > 1:
                for i in range(valLength):
                    for j in range(i+1, valLength):
                        if abs(d[key][i]-d[key][j]) <= k:
                            return True
        return False
