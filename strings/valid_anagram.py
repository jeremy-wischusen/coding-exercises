'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Solution
Approach #1 (Sorting) [Accepted]
Algorithm

An anagram is produced by rearranging the letters of ss into tt. Therefore, if tt is an anagram of ss, sorting both strings will result in two identical strings. Furthermore, if ss and tt have different lengths, tt must not be an anagram of ss and we can return early.

public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    char[] str1 = s.toCharArray();
    char[] str2 = t.toCharArray();
    Arrays.sort(str1);
    Arrays.sort(str2);
    return Arrays.equals(str1, str2);
}
Complexity analysis

Time complexity : O(n \log n)O(nlogn). Assume that nn is the length of ss, sorting costs O(n \log n)O(nlogn) and comparing two strings costs O(n)O(n). Sorting time dominates and the overall time complexity is O(n \log n)O(nlogn).

Space complexity : O(1)O(1). Space depends on the sorting implementation which, usually, costs O(1)O(1) auxiliary space if heapsort is used. Note that in Java, toCharArray() makes a copy of the string so it costs O(n)O(n) extra space, but we ignore this for complexity analysis because:

It is a language dependent detail.
It depends on how the function is designed. For example, the function parameter types can be changed to char[].
Approach #2 (Hash Table) [Accepted]
Algorithm

To examine if tt is a rearrangement of ss, we can count occurrences of each letter in the two strings and compare them. Since both ss and tt contain only letters from a-za−z, a simple counter table of size 26 is suffice.

Do we need two counter tables for comparison? Actually no, because we could increment the counter for each letter in ss and decrement the counter for each letter in tt, then check if the counter reaches back to zero.

public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    int[] counter = new int[26];
    for (int i = 0; i < s.length(); i++) {
        counter[s.charAt(i) - 'a']++;
        counter[t.charAt(i) - 'a']--;
    }
    for (int count : counter) {
        if (count != 0) {
            return false;
        }
    }
    return true;
}
Or we could first increment the counter for ss, then decrement the counter for tt. If at any point the counter drops below zero, we know that tt contains an extra letter not in ss and return false immediately.

public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    int[] table = new int[26];
    for (int i = 0; i < s.length(); i++) {
        table[s.charAt(i) - 'a']++;
    }
    for (int i = 0; i < t.length(); i++) {
        table[t.charAt(i) - 'a']--;
        if (table[t.charAt(i) - 'a'] < 0) {
            return false;
        }
    }
    return true;
}
Complexity analysis

Time complexity : O(n)O(n). Time complexity is O(n)O(n) because accessing the counter table is a constant time operation.

Space complexity : O(1)O(1). Although we do use extra space, the space complexity is O(1)O(1) because the table's size stays constant no matter how large nn is.

Follow up

What if the inputs contain unicode characters? How would you adapt your solution to such case?

Answer

Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.
'''


class Solution:
    def solve(self, s: str, t: str) -> bool:
        if len(t) != len(t):
            return False
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()

        return list_s == list_t


'''
pytest
'''
solution = Solution()


def test_is_anagram():
    assert solution.solve('anagram', 'nagaram') == True


def test_is_not_anagram():
    assert solution.solve('rat', 'car') == False
