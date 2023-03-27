my_string = "RACECAR_!Racecar"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()        
        return new_string == new_string[::-1]
    
s = Solution()
res = s.isPalindrome(my_string)

print(res)