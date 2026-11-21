class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: 
                r -= 1
        return res



    # the calculation must be two pointer
    # check the equation for width (highest array - 1) and height (min of both values), so it can store the 2 and do calculation
    # check if the area computed is less, if the max/min are smaller shift or if height are smaller shift








    # res = 0
    # for l in range (len(height)):
    #     for r in range (l + 1, len(height)):
    #              area = (r - 1) * min(height[l], height[r])
    #              res = max(res, area)

    # brute force solution, loop through each one by one