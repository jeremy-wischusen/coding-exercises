#!/usr/bin/python
'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


Solution
If an interviewer gives you this problem, your first question should be - how should I handle duplicates? Your second question, perhaps, can be about the order of inputs and outputs. Such questions manifest your problem-solving skills, and help you steer to the right solution.

The solution for the previous problem, 349. Intersection of Two Arrays, talks about approaches when each number in the output must be unique. For this problem, we need to adapt those approaches so that numbers in the result appear as many times as they do in both arrays.

Approach 1: Hash Map
For the previous problem, we used a hash set to achieve a linear time complexity. Here, we need to use a hash map to track the count for each number.

We collect numbers and their counts from one of the arrays into a hash map. Then, we iterate along the second array, and check if the number exists in the hash map and its count is positive. If so - add the number to the result and decrease its count in the hash map.

Hash Map Illustration

It's a good idea to check array sizes and use a hash map for the smaller array. It will reduce memory usage when one of the arrays is very large.

Algorithm

If nums1 is larger than nums2, swap the arrays.

For each element in nums1:

Add it to the hash map m.

Increment the count if the element is already there.
Initialize the insertion pointer (k) with zero.

Iterate along nums2:

If the current number is in the hash map and count is positive:

Copy the number into nums1[k], and increment k.

Decrement the count in the hash map.

Return first k elements of nums1.

For our solutions here, we use one of the arrays to store the result. As we find common numbers, we copy them to the first array starting from the beginning. This idea is from this solution by sankitgupta.
public int[] intersect(int[] nums1, int[] nums2) {
    if (nums1.length > nums2.length) {
        return intersect(nums2, nums1);
    }
    HashMap<Integer, Integer> m = new HashMap<>();
    for (int n : nums1) {
        m.put(n, m.getOrDefault(n, 0) + 1);
    }
    int k = 0;
    for (int n : nums2) {
        int cnt = m.getOrDefault(n, 0);
        if (cnt > 0) {
            nums1[k++] = n;
            m.put(n, cnt - 1);
        }
    }
    return Arrays.copyOfRange(nums1, 0, k);
}

Complexity Analysis

Time complexity: \mathcal{O}(n + m)O(n+m), where nn and mm are the lengths of the arrays. We iterate through the first, and then through the second array; insert and lookup operations in the hash map take a constant time.

Space complexity: \mathcal{O}(\min(n, m))O(min(n,m)). We use hash map to store numbers (and their counts) from the smaller array.

Approach 2: Sort
You can recommend this method when the input is sorted, or when the output needs to be sorted. Here, we sort both arrays (assuming they are not sorted) and use two pointers to find common numbers in a single scan.

Sort Illustration

Algorithm

Sort nums1 and nums2.

Initialize i, j and k with zero.

Move indices i along nums1, and j through nums2:

Increment i if nums1[i] is smaller.

Increment j if nums2[j] is smaller.

If numbers are the same, copy the number into nums1[k], and increment i, j and k.

Return first k elements of nums1.
public int[] intersect(int[] nums1, int[] nums2) {
    Arrays.sort(nums1);
    Arrays.sort(nums2);
    int i = 0, j = 0, k = 0;
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            ++i;
        } else if (nums1[i] > nums2[j]) {
            ++j;
        } else {
            nums1[k++] = nums1[i++];
            ++j;
        }
    }
    return Arrays.copyOfRange(nums1, 0, k);
}

Complexity Analysis

Time complexity: \mathcal{O}(n\log{n} + m\log{m})O(nlogn+mlogm), where nn and mm are the lengths of the arrays. We sort two arrays independently, and then do a linear scan.

Space complexity: \mathcal{O}(1)O(1). We sort the arrays in-place. We ignore the space to store the output as it is not essential to the algorithm itself.

Approach 3: Built-in Intersection
This is similar to Approach 2. Instead of iterating with two pointers, we use a built-in function to find common elements. In C++, we can use set_intersection for sorted arrays (or multisets).

The retainAll method in Java, unfortunately, does not care how many times an element occurs in the other collection. You can use the retainOccurrences method of the multiset implementation in Guava.

Algorithm

Note that set_intersection returns the position past the end of the produced range, so it can be used as an input for the erase function. The idea is from this solution by StefanPochmann.
vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    sort(begin(nums1), end(nums1));
    sort(begin(nums2), end(nums2));
    nums1.erase(set_intersection(begin(nums1), end(nums1), 
        begin(nums2), end(nums2), begin(nums1)), end(nums1));
    return nums1;
}

Complexity Analysis

Same as for approach 2 above.
Follow-up Questions
What if the given array is already sorted? How would you optimize your algorithm?

We can use either Approach 2 or Approach 3, dropping the sort of course. It will give us linear time and constant memory complexity.
What if nums1's size is small compared to nums2's size? Which algorithm is better?

Approach 1 is a good choice here as we use a hash map for the smaller array.
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

If nums1 fits into the memory, we can use Approach 1 to collect counts for nums1 into a hash map. Then, we can sequentially load and process nums2.

If neither of the arrays fit into the memory, we can apply some partial processing strategies:

Split the numeric range into subranges that fits into the memory. Modify Approach 1 to collect counts only within a given subrange, and call the method multiple times (for each subrange).

Use an external sort for both arrays. Modify Approach 2 to load and process arrays sequentially.

Analysis written by: @votrubac.
'''


class Solution:
    def solve(self, nums1, nums2):
        # approach: sort two lists and use two pointers to compare

        nums1.sort()
        nums2.sort()

        p1 = p2 = 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]
            num2 = nums2[p2]

            if num1 < num2:
                p1 += 1
            elif num1 > num2:
                p2 += 1
            else:
                result.append(num1)
                p1 += 1
                p2 += 1

        return result


'''
pytest tests
'''
solution = Solution()
'''
Input: nums1 = , nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

'''


def test_case_1():
    assert solution.solve([1, 2, 2, 1], [2, 2]) == [2, 2]


def test_case_2():
    assert solution.solve([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
