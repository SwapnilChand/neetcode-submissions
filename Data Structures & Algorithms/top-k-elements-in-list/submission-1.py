# Input: nums = [1, 1, 2,2,2, 3,3,3], k = 2

# Output: [2,3]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        # number -> freq
        freq = [[] for _ in range(len(nums) + 1)]
        # [[], [], [], [], [], [] ,[], []]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # count = {1: 2, 2: 3, 3: 3}
        for num, cnt in count.items():
            freq[cnt].append(num)
        # [[], [1], [2, 3], [], [], [] ,[], []]

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res


