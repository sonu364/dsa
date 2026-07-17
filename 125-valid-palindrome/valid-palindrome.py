class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string using separate lines
        cleaned_list = []
        for char in s:
            if char.isalnum():
                cleaned_list.append(char.lower())
        
        cleaned_s = "".join(cleaned_list)
        
        # 2. Reverse the cleaned string
        r = cleaned_s[::-1]
        
        # 3. Compare and return
        return cleaned_s == r