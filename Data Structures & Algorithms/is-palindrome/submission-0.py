class Solution:
    def isPalindrome(self, s: str) -> bool:

        ss = "".join(ch for ch in s if ch.isalnum())

        for i in range(math.floor(len(ss)/2)):
            if ss[i].lower() != ss[len(ss) - 1 - i].lower():
                return False
        
        return True