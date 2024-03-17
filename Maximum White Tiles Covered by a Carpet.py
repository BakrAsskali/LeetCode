from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        floor = []
        maxlen = 0
        for tile in tiles:
            for tileLen in range(tile[0], tile[1]+1):
                if tileLen not in floor:
                    floor.append(tileLen)
        floor.sort()
        currentLen = 0
        for i in range(len(floor) - 1):
            if floor[i + 1] == floor[i] + 1:
                currentLen = currentLen + 1
                if currentLen > carpetLen:
                    currentLen = carpetLen
            else:
                currentLen = 0
            maxlen = max(maxlen, currentLen)
        maxlen += 1
        print(floor)
        print(maxlen)
        return maxlen


sol = Solution()

if sol.maximumWhiteTiles([[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], 10) == 9:
    print("Test case 1 passed")

if sol.maximumWhiteTiles([[10, 11], [1, 1]], 2) == 2:
    print("Test case 2 passed")

if sol.maximumWhiteTiles(
        [[8051, 8057], [8074, 8089], [7994, 7995], [7969, 7987], [8013, 8020], [8123, 8139], [7930, 7950], [8096, 8104],
         [7917, 7925], [8027, 8035], [8003, 8011]], 9854) == 126:
    print("Test case 3 passed")
