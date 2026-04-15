# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(0 ,len(nums) + 1)]

        for num in nums:        
            # print(num)
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res
