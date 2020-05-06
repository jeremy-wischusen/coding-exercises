"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution:
    def solve(self, l1: list, l2: list) -> float:
        combined = l1+l2
        combined.sort()
        l = len(combined)
        mid = l//2
        if l % 2 == 0:
            return (combined[mid-1] + combined[mid])/2
        else:
            return combined[mid]


''' pytest '''
solution = Solution()


def test_case_1():
    assert solution.solve([1, 2], [3]) == 2


def test_case_2():
    assert solution.solve([1, 2], [3, 4]) == 2.5
