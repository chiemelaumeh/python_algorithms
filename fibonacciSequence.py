class Solution(object):

 def fibbonacciSequence(self,n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fibSeq = [0, 1]

    while len(fibSeq) < n: 
        next = fibSeq[-1] + fibSeq[-2]
        fibSeq.append(next)

    return fibSeq
 
 def returnFibSequence(self,n):
    return self.fibbonacciSequence(n)
 
callClass = Solution()
print(callClass.returnFibSequence(6))

# you may ignore the oop