class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        current_len = 0
        start_pos = 0
        end_pos = 0
        
        index_array={}
        sub_str = []
        if len(s) == 0 :
            return 0

        for char in s :
            if char in index_array and index_array[char] >= start_pos:
                if  new_length > current_len:
                    current_len = new_length
                if start_pos > index_array[char] + 1:
                    start_pos = start_pos + 1
                else:
                    start_pos = index_array[char] + 1
            index_array[char] = end_pos     
            end_pos += 1
            new_length = end_pos - start_pos
            #print("ch[%s], sp[%s], ep[%s], current_len[%s], new_length[%s]" %(char, start_pos, end_pos, current_len, new_length))
        
        if new_length > current_len:
            current_len = new_length
        #print("ch[%s], sp[%s], ep[%s], current_len[%s], new_length[%s]" %(char, start_pos, end_pos, current_len, new_length))
        return current_len
            
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring(''))
print(Solution().lengthOfLongestSubstring(' '))
print(Solution().lengthOfLongestSubstring('abba'))
print(Solution().lengthOfLongestSubstring('tmmzuxt'))
