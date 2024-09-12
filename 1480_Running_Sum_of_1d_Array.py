class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # runningSum[i] = sum(nums[0]…nums[i]).
        li = []
        for i in range(len(nums)):
            li.append(sum(nums[:i+1]))
            
        return li
