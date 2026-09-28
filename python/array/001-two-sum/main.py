class Solution:
    def twosum(self, nums:list[int], target: int) -> list[int]:
                
        self.nums = nums
        self.target = target
        
        numMap = {}
        
        for i, numero in enumerate(self.nums):
            numMap[numero] = i
        for i, numero in enumerate(self.nums):
            aux = target - numero
            
            if aux in numMap and numMap[aux] != i:
                return [i, numMap[aux]]
            
        return []
            
sol = Solution()
print(f'{sol.twosum([2,7,11,15], 9)}')
print(f'{sol.twosum([3,2,4], 6)}')
print(f'{sol.twosum([3,3], 6)}')