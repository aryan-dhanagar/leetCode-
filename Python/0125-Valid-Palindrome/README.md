# LeetCode #125 — Valid Palindrome

- **Difficulty:** Easy
- **Language:** Python
- **Runtime:** 11 ms
- **Memory:** 12.54 MB
- **Runtime Beats:** 92.61%
- **Memory Beats:** 91.72%

## Approach

1. Initialize two pointers: `left` at the beginning and `right` at the end of the string.
2. Move `left` forward while the current character is not alphanumeric.
3. Move `right` backward while the current character is not alphanumeric.
4. Convert both characters to lowercase and compare them.
5. If the characters are different, return `False`.
6. If they match, move both pointers toward the center.
7. If all valid characters match, return `True`.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Status

✅ Accepted
