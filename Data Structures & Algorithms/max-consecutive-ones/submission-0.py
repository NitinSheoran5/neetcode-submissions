class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0
        for n in nums:
            if (n == 1):
                count = count + 1
                if(count > max):
                    max = count
            else:
                count = 0
        return max


        