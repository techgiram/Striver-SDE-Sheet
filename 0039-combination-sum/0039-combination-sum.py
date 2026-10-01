class Solution(object):
    def combinationSum(self, candidates, target, current=None, result=None, index=0):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if current is None:
            current = []
        if result is None:
            result = []

        if target == 0:
            result.append(current[:])
            return result

        for i in range(index, len(candidates)):
            if candidates[i] <= target:
                current.append(candidates[i])
                targets = target - candidates[i]
                self.combinationSum(candidates, targets, current, result, i)
                current.pop()

        return result