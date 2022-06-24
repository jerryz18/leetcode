class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        counter = {}
        
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in counter:
                counter[sort] = [s]
            else:
                counter[sort].append(s)
        
        for key in counter:
            newList = []
            for val in counter[key]:
                newList.append(val)
            lst.append(newList)
            
        return lst
