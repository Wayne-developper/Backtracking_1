class solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        extend = res.extend
        for x in nums:
            extend([curr + [x] for curr in res])
        return res
            