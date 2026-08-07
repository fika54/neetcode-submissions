class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        i = 0
        j = 0
        while i < 9:
            while j < 9:
                check = board[i][j]
                if check == ".":
                    j += 1
                    continue

                if check in seen:
                    return False
                seen.add(check)
                j += 1
            i+=1
            j = 0
            seen.clear()

        
        

        i = 0
        j = 0

        while i < 9:
            while j < 9:
                check = board[j][i]
                if check == ".":
                    j += 1
                    continue
                if check in seen:
                    return False
                seen.add(check)
                j+=1
            i+=1
            j = 0
            seen.clear()

        seen.clear()

        i = 0
        j = 0
        k = 0

        while i < 9:
            while j < 9:
                row = j//3
                check = board[(i//3)*3+row][(i%3)*3+(j%3)]
                if check == ".":
                    j += 1
                    continue
                if check in seen:
                    return False
                seen.add(check)
                j += 1
                

            i+=1
            j = 0
            seen.clear()



        return True
