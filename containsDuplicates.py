
class Solution(object):
 def containsDuplicate(self,nums):
        numsSet = set()
        for i in nums:
            if i in numsSet:
                return True
            numsSet.add(i)
        return False
solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))




class Solution(object):
 def containsDuplicate(self, nums):
    nums.sort()
    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1]):
            print(nums[i])
            return True
    return False

solution = Solution()
print(solution.containsDuplicate([3,4,5,6,3]))


