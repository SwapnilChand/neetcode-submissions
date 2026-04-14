class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: 
        # nums=[0,4,3,0]
        # target=0
        # Output: [0,3]

        map = {}
        for i, num in enumerate(nums): #[i  = 0 -> num = 0, 1 -> 4, 2 -> 3 , (4 -> 0)]

            # if target - nums[i] > 0: # target = 0 , nums[i] = nums[0] = 0
            #     complement = target - num
            # else:
            #     continue
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i