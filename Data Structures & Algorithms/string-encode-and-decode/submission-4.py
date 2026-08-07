class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            encode = ''
            if word == "":
                string = string + "." + '-1'
                continue
            for c in word:
                encode = encode + "," +str(ord(c))
            string = string + "." + encode[1:]

        print(string[1:])
        return string[1:]


    def decode(self, s: str) -> List[str]:
        decoded_string = []
        
        words = s.split('.')

        for word in words:
            
            letters = word.split(',')
            finished_word = ''

            for letter in letters:
                try:
                    if letter == '-1':
                        finished_word = finished_word + ""
                        break
                    elif letter == "":
                        return []
                    finished_word = finished_word + chr(int(letter))
                except:
                    finished_word = finished_word + ''
            
            decoded_string.append(finished_word)
            

        
        return decoded_string
            

