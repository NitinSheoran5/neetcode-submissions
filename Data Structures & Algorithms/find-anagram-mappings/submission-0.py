class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myMap: dict[str, int] = {}
        result = []
        for i in range(len(nums2)):
            myMap[nums2[i]] = i
        
        for i in range(len(nums1)):
            result.append(myMap.get(nums1[i]))

        return result 
        