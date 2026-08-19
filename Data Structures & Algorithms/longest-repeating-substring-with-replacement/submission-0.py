class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #identify distinct characters
        #if the number of distinct characters go above k + 1 move on.
        #track the dominent cbar in a subset.
        unique = {}

        size = 0
        curLargest = None
        back = 0

        for i, char in enumerate(s):
            unique[char] = unique.setdefault(char, 0) + 1
            size += 1

            if not curLargest or unique[curLargest] < unique[char]:
                curLargest = char
            
            if not self.isValid(unique, k, curLargest, size):
                lchar = s[back]
                back += 1
                size -= 1
                unique[lchar] -= 1
        
        return size
    
    def isValid(self, unique: dict, k: int, largest: str, size: int):
        remainder = size - unique[largest]

        if remainder <= k:
            return True
        else:
            return False
        


