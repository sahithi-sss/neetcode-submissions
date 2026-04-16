class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #width = r-l
        #ht = min(heights[l],heights[r])

        max_area = 0
        l,r = 0, len(heights)-1
        while l<r:
            max_area = max(max_area, ((r-l)* (min(heights[r],heights[l]))))
            if heights[l] <= heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            
        return max_area