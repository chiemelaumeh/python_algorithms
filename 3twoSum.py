class Solution(object):
    def twoSum(self, nums, target):
        index_map = {} 
        for i, num in enumerate(nums):
            difference = target - num
            if difference in index_map:
                return [difference, num]  

            index_map[num] = i  
        return None

solution = Solution()
print(solution.twoSum([1, 2, 3, 4, 5], 9))  
