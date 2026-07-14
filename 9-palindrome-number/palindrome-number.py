class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes (e.g., -121 reversed is 121-)
        if x < 0:
            return False

        i = x
        s = 0

        while i > 0:
            d = i % 10
            s = s * 10 + d
            i = i // 10

        # Check if the original number equals the reversed number
        return x == s