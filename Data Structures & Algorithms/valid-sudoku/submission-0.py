from collections import defaultdict
import math

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # rows, columns, group ids
        digit_locations = defaultdict(lambda: (set(), set(), set()))
        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]
                if not value.isdigit() and value != ".":
                    return False
                if value == ".":
                    continue
                group_id = (math.floor(row/3) * 3) + math.floor(col/3)
                if row in digit_locations[value][0] or col in digit_locations[value][1] or group_id in digit_locations[value][2]:
                    return False
                digit_locations[value][0].add(row)
                digit_locations[value][1].add(col)
                digit_locations[value][2].add(group_id)
        return True