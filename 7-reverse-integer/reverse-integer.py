class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        i = abs(x)
        s = 0

        while i > 0:
            d = i % 10
            s = s * 10 + d
            i = i // 10

        s = s * sign 
        if s < -2**31 or s > 2 **31 -1:
            return 0
        return s 