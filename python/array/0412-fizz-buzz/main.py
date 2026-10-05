class Solution:
    
    def fizzBuzz(self, n: int) -> list[str]:
        
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and n % 5 == 0:
                answer.append("FizzBuzz")
        
            elif i % 3 == 0:
                answer.append("Fizz")
        
            elif i % 5 == 0:
                answer.append("Buzz")
        
            else:
                answer.append(str(i))
        
        return answer


teste = Solution()
print(f'{teste.fizzBuzz(3)}')
print(f'{teste.fizzBuzz(5)}')
print(f'{teste.fizzBuzz(15)}')