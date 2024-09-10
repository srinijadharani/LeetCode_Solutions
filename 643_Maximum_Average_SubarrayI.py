class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        current_sum = 0

        # initialize the sliding window
        for i in range(k):
            current_sum += nums[i]
        
        # initialize the max average
        max_average = float(current_sum) / k

        # start sliding by k
        for i in range(k, n):   
            # need to add one to the existing sum
            current_sum += nums[i]
            # need to remove one from the existing sum, the one that was in the previous iteration
            current_sum -= nums[i-k]

            average = float(current_sum) / k
            max_average = max(max_average, average)

        return max_average        
