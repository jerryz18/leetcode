class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        row = []
        
        if numRows == 0:
            return triangle
        
        row.append(1)
        triangle.append(row)
        
        if numRows == 1:
            return triangle
        else:
            for i in range(1, numRows):
                prev = triangle[i-1]
                curr = []
                curr.append(1)
                for j in range(0, i-1):
                    curr.append(prev[j] + prev[j+1])
                curr.append(1)
                triangle.append(curr)
            return triangle
   
