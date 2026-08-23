# LeetCode #344 — Reverse String

* **Difficulty:** Easy
* **Language:** Python
* **Runtime:** 6 ms
* **Memory:** 19.64 MB
* **Runtime Beats:** 20.78%
* **Memory Beats:** 98.00%

## Approach

1. Initialize two pointers: `left` at the beginning and `right` at the end of the list.
2. While `left < right`, swap the elements at `left` and `right`.
3. Move `left` one position forward.
4. Move `right` one position backward.
5. Continue until the two pointers meet or cross.
6. The string is reversed **in-place** without creating another list.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Status

✅ Accepted
