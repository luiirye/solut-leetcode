class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        
        numMap = {}
        
        for i, numero in enumerate(nums):
            numMap[numero] = i
        for i, numero in enumerate(nums):
            aux = target - numero
            
            if aux in numMap and numMap[aux] != i:
                return [i, numMap[aux]]
            
        return []
            
sol = Solution()
print(f'{sol.twoSum([2,7,11,15], 9)}')
print(f'{sol.twoSum([3,2,4], 6)}')
print(f'{sol.twoSum([3,3], 6)}')