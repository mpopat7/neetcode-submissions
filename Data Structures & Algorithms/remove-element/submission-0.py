class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        x= len(nums)
        for i in range(0, len(nums)):
            if nums[i-k] == val:
                nums.remove(nums[i-k])
                k=k+1
                
            
                
        return x - k
        
        