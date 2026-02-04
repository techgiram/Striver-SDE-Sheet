class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        INF = -(10**18)
        memo = {}

        def dfs(i, state):
            if (i, state) in memo:
                return memo[(i, state)]

            if i == n:
                return 0 if state == 3 else INF

            res = INF

            if state == 0:
                if i + 1 < n and nums[i] < nums[i + 1]:
                    res = nums[i] + dfs(i + 1, 1)

            elif state == 1:
                if i + 1 < n and nums[i] < nums[i + 1]:
                    res = max(res, nums[i] + dfs(i + 1, 1))
                if i + 1 < n and nums[i] > nums[i + 1]:
                    res = max(res, nums[i] + dfs(i + 1, 2))

            elif state == 2:
                if i + 1 < n and nums[i] > nums[i + 1]:
                    res = max(res, nums[i] + dfs(i + 1, 2))
                if i + 1 < n and nums[i] < nums[i + 1]:
                    res = max(res, nums[i] + dfs(i + 1, 3))

            else:  # state == 3
                res = nums[i]
                if i + 1 < n and nums[i] < nums[i + 1]:
                    res = max(res, nums[i] + dfs(i + 1, 3))

            memo[(i, state)] = res
            return res

        ans = INF
        for i in range(n):
            ans = max(ans, dfs(i, 0))

        return ans
