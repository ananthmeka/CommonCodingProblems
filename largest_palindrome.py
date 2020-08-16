class Solution:
    position_dict = {}
    largest_palindrome = ""
    def longestPalindrome(self, s: str) -> str:
        index = 1
        length = len(s)
        if length == 1 or length == 0:
            return s
        if length == 2:
            if s[0] != s[1]:
                return s[0]
            return s
        else:
            self.largest_palindrome = s[0]
            
        while index < length-1:
            if s[index] == s[index-1]:
                self.get_pailndrome(s, length, index, True)
            if s[index-1] == s[index+1]:
                self.get_pailndrome(s, length, index, False)
            index += 1
        if s[length-1] == s[length-2] and len(self.largest_palindrome) < 2:
            return s[length-2:]
        return self.largest_palindrome
    
    def get_pailndrome(self, s:str, length:int, index:int, doubleword: bool) -> str:
        palindrome_string = ""
        min_index = index-1
        if doubleword:

            max_index = index
        else:
            max_index = index+1
            
        while min_index >=0 and max_index <= length-1:
            if s[min_index] == s[max_index]:
                min_index -= 1
                max_index += 1
            else:
                break;
        palindrome_string = s[min_index+1 : max_index]

        if len(palindrome_string) > len(self.largest_palindrome):
            self.largest_palindrome = palindrome_string

#print(Solution().longestPalindrome("abba"))      
#print(Solution().longestPalindrome("ayzabbacd"))      
#print(Solution().longestPalindrome("ayzabbacdxdcay"))      
#print(Solution().longestPalindrome("baba"))      
print(Solution().longestPalindrome("abb"))      

