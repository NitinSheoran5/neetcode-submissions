class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatArr = []
        self.insertData(nums, concatArr)
        self.insertData(nums, concatArr)
        return concatArr

    
    def insertData(self, nums: List[int], concatArr: List[int]) -> None:
        for i in nums:
            concatArr.append(i)
        