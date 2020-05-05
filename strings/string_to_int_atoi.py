'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''


class Solution:
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    def solve(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = None
        if s[0] in '-+':
            sign = s[0]
            s = s[1:]

        if not s or not s[0].isdigit():
            return 0

        end = 0
        for i in s:
            if i.isdigit():
                end += 1
            else:
                break

        s = s[:end]

        if sign is not None:
            s = '{}{}'.format(sign, s)

        i = int(s)
        if i > self.INT_MAX:
            return self.INT_MAX
        elif i < self.INT_MIN:
            return self.INT_MIN
        else:
            return i


'''
pytest
'''
solution = Solution()


def test_case_1():
    assert solution.solve('42') == 42


def test_case_2():
    assert solution.solve("   -42") == -42


def test_case_3():
    assert solution.solve("4193 with words") == 4193


def test_case_4():
    assert solution.solve('words and 987') == 0


def test_case_6():
    assert solution.solve("-91283472332") == Solution.INT_MIN


def test_case_6():
    assert solution.solve("91283472332") == Solution.INT_MAX


def test_case_7():
    assert solution.solve('+42') == 42


def test_case_8():
    assert solution.solve(' ') == 0
