class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = n
        pos = 0
        for i in range(n):
            if(nums[i] != val):
                if(pos != i):
                    nums[pos] = nums[i]
                pos = pos+1
            else:
                k = k-1
        return k

            
        