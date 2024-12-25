# # Algo to find the most occuring number is a list
# class Solution(object):
    
#  def countOccurences(self, nums):
#     countDict = {}
#     for num in nums:
#         if num in countDict:
#             countDict[num]+=1
#         else:
#             countDict[num] = 1
#     # print(countDict)
#     highestOccuringNum = None
#     maxCount = 0
#     for num, count in countDict.items():
#         if count > maxCount:
#             maxCount = count
#             highestOccuringNum = num


#     return highestOccuringNum, maxCount
# callSolution = Solution()
# print(callSolution.countOccurences([1,2,3,4,5,2,4,6,4]))


def countNums(nums):
    countDict = {}
    for num in nums:
   
        if num in countDict:
            countDict[num]+=1
        else:
            countDict[num] = 1
    maxCount = 0
    highestOccuringNum = None

    for num, count in countDict.items():
        print(num)

        if count > maxCount:
          maxCount = count
          highestOccuringNum = num
    return highestOccuringNum, maxCount
print(countNums([1,2,3,4,5,2,4,6,4]))
