class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        maps = dict()

        if len(s) != len(t):
            return False

        for i in s:
            if i in maps:
                maps[i] = maps[i] + 1
            else:
                maps[i] = 1

        for i in t:
            if i not in maps:
                return False
            
            maps[i] = maps[i] - 1

            if maps[i] < 0:
                return False

        return True
        