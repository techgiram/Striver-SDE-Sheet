class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        lp = 0
        rp = len(height) - 1

        while lp < rp:
            width = rp - lp
            ht = min(height[lp],height[rp])
            currWater = width * ht

            maxWater = max(maxWater , currWater)

            if height[lp] < height[rp]:
                lp+=1
            else:
                rp-=1
        return maxWater
