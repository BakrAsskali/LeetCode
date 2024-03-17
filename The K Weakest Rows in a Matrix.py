from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_soldiers = 0
        weakest_array = []
        soldier_dict = {}
        row_num = 0
        for row in mat:
            for column in row:
                if column == 1:
                    num_soldiers += 1
                    continue
                else:
                    continue
            soldier_dict[row_num] = num_soldiers
            num_soldiers = 0
            row_num += 1
        for i in range(k):
            weakest_array.append(min(soldier_dict, key=soldier_dict.get))
            soldier_dict.pop(min(soldier_dict, key=soldier_dict.get))
        print(weakest_array)
        return weakest_array


sol = Solution()

if sol.kWeakestRows([[1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1]], 3) == [2, 0, 3]:
    print("Test case 1 passed")

if sol.kWeakestRows([[1, 0, 0, 0],
                     [1, 1, 1, 1],
                     [1, 0, 0, 0],
                     [1, 1, 0, 0]], 2) == [0, 2]:
    print("Test case 2 passed")

if sol.kWeakestRows([[1, 0],
                     [1, 0],
                     [1, 0],
                     [1, 1]], 4) == [0, 1, 2, 3]:
    print("Test case 3 passed")
