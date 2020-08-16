class Solution:
    def reverse(self, x: int) -> int:
        val = 0
        y = str(x)
        if x < 0:
            z = y[:0:-1]
            a = int(z)
            val = -a
        else:
            z = y[::-1]
            val = int(z)
        limit = pow(2,31)
        if val <= limit-1 and val >= -limit:
           return val
        else:
          return 0

print(Solution().reverse(-200))
