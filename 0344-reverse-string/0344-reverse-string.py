class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)

        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
       