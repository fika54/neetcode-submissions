class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        subfreq = [0] * 26
        stringfreq = [0] * 26

        for char in s1:
            letter = ord(char) - ord('a')

            subfreq[letter] += 1
        
        i = 0
        j = len(s1) - 1

        if len(s1) > len(s2):
            return False
        

        while i <= j:
            letter = ord(s2[i]) - ord('a')
            stringfreq[letter] += 1
            i += 1 

        i = 0

        while j < len(s2):
            if self.isValid(subfreq, stringfreq):
                return True
            
            if j < len(s2) - 1:
                letter = ord(s2[i]) - ord('a')
                stringfreq[letter] -= 1
                i += 1
                j += 1
                letter = ord(s2[j]) - ord('a')
                stringfreq[letter] += 1
            else:
                j += 1

        

        return False      



    def isValid(self, subArray, stringArray):
        i = 0
        while i < len(subArray):
            if subArray[i] != stringArray[i]:
                return False
            i += 1
            
        return True
