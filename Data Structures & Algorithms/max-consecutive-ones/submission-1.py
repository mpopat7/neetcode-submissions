class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0
        max = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                ct +=1
            else:
                if ct > max:
                    max = ct
                ct= 0
        if ct > max:
            max = ct
        return max


        