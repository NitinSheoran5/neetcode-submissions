class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        myMap = {}
        for n in nums:
            if(n not in myMap):
                myMap[n] = 1
            else:
                myMap[n] = myMap[n]+1
        
        flag = False
        max = 0
        for key in myMap:
            if(myMap[key] == 1 and key > max):
                max = key
                flag = True
        
        if(flag == True):
            return max
        else:
            return -1