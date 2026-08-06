# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         out = []
#         anagramDict = {}

#         for word in strs:
#             freqKey = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#             for letter in word:
#                 index = self.letterToNum(letter)
#                 freqKey[index] = freqKey[index] + 1
            
#             key = ''
#             for num in freqKey:
#                 key = key + str(num) + ','
            
            
            

#             if key in anagramDict:
#                 anagramDict[key].append(word)
#             else:
#                 anagramDict[key] = [word]

#         for keys in anagramDict:
#             out.append(anagramDict[keys])
        
#         return out


#     def letterToNum(self, letter: str):
#         alphabet = "abcdefghijklmnopqrstuvwxyz"

#         i = 0
#         for i in range(len(alphabet)):
#             if alphabet[i] == letter:
#                 return i
#             i = i + 1
        
#         return 27
                

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
                