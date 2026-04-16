class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lst = []
        l,r = 0, len(heights)-1
        while l<r:
            a,b= heights[l],heights[r]
            lst.append((min(a,b))* (r-l))
            
            if a<b:
                l+= 1
            else:
                r-=1
        
        return max(lst)