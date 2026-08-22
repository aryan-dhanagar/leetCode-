# LeetCode #7 — Reverse Integer

- Difficulty: Medium
- Language: Python
- Runtime: 11 ms
- Memory: 12.25 MB
- Runtime Beats: 92.48%
- Memory Beats: 87.75%

## Approach

1. Handle negative numbers.
2. Extract the last digit using `% 10`.
3. Build the reversed number.
4. Remove the last digit using `// 10`.
5. Check the 32-bit integer range.

## Complexity

- Time: O(log n)
- Space: O(1)

## Status

✅ Accepted