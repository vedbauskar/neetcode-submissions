class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key is (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r// 3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True



# context
# need to scan each row and colum n containing 1-9 without duplicates
# each of the nine 3x3 must contain the digits 1-9 without duplicates
# return true if valid, otherwise return false
# board lenght is only 9, digit 1-9 or .

# test cases
# input can be "." or not full
# 


# implenetation
# create a hashset for both checking rows, columns, and 3x3 (must be all true)
# in the instance 
# create a hashset for checking each 3x3 column
#       0     1      2      3      4      5      6      7      8
#
# 0   (0,0) (0,0)  (0,0)  (0,1)  (0,1)  (0,1)  (0,2)  (0,2) (0,2)
#
# 1   (0,0) (0,0)  (0,0)  (0,1)  (0,1)  (0,1)  (0,2)  (0,2) (0,2)
#
# 2   (0,0) (0,0)  (0,0)  (0,0)  (0,1)  (0,1)  (0,2)  (0,2) (0,2)
#
# 3   (1,0) (1,0)  (1,0)  (1,1)  (1,1)  (1,1)  (1,2)  (1,2) (1,2)
# 
# 4   (1,0) (1,0)  (1,0)  (1,1)  (1,1)  (1,1)  (1,2)  (1,2) (1,2)
#
# 5   (1,0) (1,0)  (1,0)  (1,1)  (1,1)  (1,1)  (1,2)  (1,2) (1,2)
#
# 6   (2,0) (2,0)  (2,0)  (2,1)  (2,1)  (2,1)  (2,2)  (2,2)  (2,2)
#
# 7   (2,0) (2,0)  (2,0)  (2,1)  (2,1)  (2,1)  (2,2)  (2,2)  (2,2)
#
# 8   (2,0) (2,0)  (2,0)  (2,1)  (2,1)  (2,1). (2,2)  (2,2) (2,2)

#each square will have a key that names the box, each set will then have digits and will check if the digits are duplicate within the set.

# if found false, else return true
# 