class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7
        # Output: [0,1]
        map = {}
        for i, num in enumerate(nums): # i = 1 , num = 4
            complement = target - num # 3
            if complement in map:
                return [map[complement], i]
            map[num] = i