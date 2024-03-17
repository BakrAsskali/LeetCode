class Solution:
    def romanToInt(self, s: str) -> int:
        i_count = 0
        x_count = 0
        c_count = 0
        number = 0
        for i in range(len(s)):
            if s[i] == 'I':
                i_count += 1
                number += 1
            elif s[i] == 'V':
                if i_count > 0:
                    number += 3
                    i_count = 0
                else:
                    number += 5
            elif s[i] == 'X':
                if i_count > 0:
                    number += 8
                    i_count = 0
                else:
                    number += 10
                    x_count += 1
            elif s[i] == 'L':
                if x_count > 0:
                    number += 30
                    x_count = 0
                else:
                    number += 50
            elif s[i] == 'C':
                if x_count > 0:
                    number += 80
                    x_count = 0
                else:
                    number += 100
                    c_count += 1
            elif s[i] == 'D':
                if c_count > 0:
                    number += 300
                    c_count = 0
                else:
                    number += 500
            elif s[i] == 'M':
                if c_count > 0:
                    number += 800
                    c_count = 0
                else:
                    number += 1000
        return number
