class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # 1. If left character is not a letter/number, skip it
            if not s[left].isalnum():
                left += 1
                
            # 2. If right character is not a letter/number, skip it
            elif not s[right].isalnum():
                right -= 1
                
            # 3. If both are letters/numbers, compare them
            else:
                if s[left].lower() != s[right].lower():
                    return False  # Not a match!
                left += 1
                right -= 1
                
        return True