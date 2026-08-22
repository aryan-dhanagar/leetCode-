# LeetCode #9 — Palindrome Number

* **Difficulty:** Easy
* **Language:** Python
* **Runtime:** 10 ms
* **Memory:** 12.41 MB
* **Runtime Beats:** 60.09%
* **Memory Beats:** 18.67%

## Approach

1. Store the original number in `copy`.
2. If the number is negative, return `False`.
3. Reverse the number by extracting each digit using `% 10`.
4. Build the reversed number using:
   `rev = rev * 10 + digit`
5. Remove the last digit using `// 10`.
6. Compare the reversed number with the original number.
7. If both are equal, the number is a palindrome.

## Complexity

* **Time:** O(log₁₀ n)
* **Space:** O(1)

## Status

✅ Accepted
