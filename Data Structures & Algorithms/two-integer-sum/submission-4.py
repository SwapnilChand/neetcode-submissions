class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: 
        # nums = [3,4,5,6], target = 7
        # Output: [0,1]
        map = {}
        for i, num in enumerate(nums):      # 1, 4
            compliment = target - num       # 3
            if compliment in map:           
                return [map[compliment], i] # return [map[3], 1] = [0, 1]
            map[num] = i             # map[4] = 1 | {"4", 1}