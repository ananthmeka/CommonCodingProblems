class Solution:
    def convert(self, s: str, numRows: int) -> str:
        current_pos = 1
        final_string = ""
        output = {}
        if len(s) == 0:
            return final_string
        if numRows == 1:
            return s
        for char in s:
            if current_pos in output:
                output[current_pos] = output[current_pos] + char
            else:
                output[current_pos] = char
            
            if current_pos == numRows:
                direction = -1
            if current_pos == 1:
                direction = 1
            current_pos += direction
        index = 1
        while index <= numRows:
            if index in output:
                final_string = final_string + output[index]
            index += 1
        return final_string
            
