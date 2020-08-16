class Solution:
    def isPalindrome(self, x: int) -> bool:
        base = 10
        int_string = str(x)
        length = len(int_string)
        half_length = int(length/2)
        limit = length-1
        i = 0
        while i < half_length :
            if int_string[i] != int_string[limit-i]:
                break;
            i += 1
        if i == half_length:
            return True
        return False
        
