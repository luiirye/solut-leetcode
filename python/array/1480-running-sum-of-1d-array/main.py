class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        soma = 0
        running_sum = []

        for numero in nums:
            soma += numero
            running_sum.append(soma)

        return running_sum
    
teste = Solution()
print(f'{teste.runningSum([1,2,3,4])}')
print(f'{teste.runningSum([1,1,1,1,1,])}')
print(f'{teste.runningSum([3,1,2,10,1])}')