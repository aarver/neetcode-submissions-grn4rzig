class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        sorted_freq = list(sorted(freq.items(), key = lambda x: x[1], reverse=True))

        l = []
        for i in range(k):
            l.append(sorted_freq[i][0])

        return l
            