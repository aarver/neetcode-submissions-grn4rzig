class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     n = nums[i]
        #     index = i
        #     for i in range(len(nums)):
        #         if nums[i] == n and i != index:
        #             return True
        #             break
        
        # return False
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return True

        return False