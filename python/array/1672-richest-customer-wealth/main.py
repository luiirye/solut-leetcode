class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
       
        max = 0
        
        for i in range(len(accounts)):
            
            customerWealth = 0
            
            for j in range(len(accounts[i])):
                customerWealth += accounts[i][j]
                
            if max < customerWealth:
                max = customerWealth
                
        return max