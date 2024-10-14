class Solution(object):
   
 def missingNumber(self, nums):
   n = len(nums) + 1
   totalNum = n*(n+1)//2
   totalMissingNum = sum(nums)
   return totalNum - totalMissingNum
solution = Solution()


print(solution.missingNumber([1,2,3,5]))

# //I take advantage that the sum of an arithmetic series from 1 to n is = n*(n+1)//2
