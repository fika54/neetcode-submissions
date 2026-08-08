class Solution:
    def isPalindrome(self, s: str) -> bool:

        front = 0
        back = len(s) - 1

        while front < back:
            while front < back and s[front].isalnum() != True:
                front += 1
            
            while back > front and s[back].isalnum() != True:
                back -= 1

            # if front >= len(s) or back < 0:
            #     break
            
            if s[front].lower() != s[back].lower():
                return False
            
            front += 1
            back -= 1
        
        return True