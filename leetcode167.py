numbers = [2,7,11,15] 
target = 9

class Solution:
    def twoSum(self, numbers):
        l, r = 0, len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
    
s = Solution()
print(s.twoSum(numbers))