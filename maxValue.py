class Solution(object): 
 def maxValue(self, nums):
    if not nums:
        return None
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max
callSolution = Solution()



print(callSolution.maxValue([1,2,3,4,9,24,6,1,6,8,5]))