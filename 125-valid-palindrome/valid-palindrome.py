class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string: keep only alphanumeric characters and make them lowercase
        cleaned_s = "".join(char.lower() for char in s if char.isalnum())
        
        # 2. Reverse the cleaned string
        r = cleaned_s[::-1]
        
        # 3. Compare and return
        return cleaned_s == r