from typing import List


class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        mydict = {}
        temp_dict = {}

        for num in balls:
            mydict[num] = mydict.get(num, 0) + 1

        max_count = max(mydict.values())
        min_count = min(mydict.values())

        while max_count - min_count > 1:
            for key in mydict:
                if mydict[key] == max_count:
                    mydict[key] -= 1
                    temp_dict[key] = temp_dict.get(key, 0) + 1
                    break
            max_count = max(max(mydict.values()), max(temp_dict.values()))
            min_count = min(min(mydict.values()), min(temp_dict.values()))

        return len(mydict) + len(temp_dict)


sol = Solution()


if sol.minGroupsForValidAssignment([1, 2, 3, 3, 3, 3, 3]) == 5:
    print("Test case 2 passed")

