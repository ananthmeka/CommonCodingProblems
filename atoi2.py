class Solution:
    def myAtoi(self, str: str) -> int:
    
        i = 0
        value = 0
        
        if str == "":
            return 0
        
        length = len(str)

        while i < length and str[i] == ' ':
            i += 1

          
        negate = False
        
        if i != len(str):
 
            new_str = str[i:]

        
            if (new_str[0] < '0' or new_str[0] > '9') and new_str[0] != '-' and new_str[0] != '+':
                return 0

            string_list = new_str.split(' ')
            value = 0
            first_string = string_list[0]

            
            if first_string[0] == '-' or first_string[0] == '+' :
                if len(first_string) == 1:
                    return 0
                
                if first_string[1] < '0' or  first_string[1] > '9':
                    return 0
                
                if first_string[0] == '-' :   #negate
                    negate = True
                    
                first_string = first_string[1:]
                
            try: 
                i = 0
                length = len(first_string)
                dotFound = False
                while i < length and ((first_string[i] >= '0' and  first_string[i] <= '9') or first_string[i] == '.'):
                    if first_string[i] == '.':
                        if dotFound == True:
                            return 0

                        dot_pos = i
                        dotFound = True
                    i += 1
                    
                first_string = first_string[0:i]

                if len(first_string) == 0:
                    return 0
                
                if '.' in first_string:     # Float check
                    value = float(first_string)
                    value = int(value)
                else:
                    value = int(first_string)
                    
            except Exception as ex:
                print("Exception : %s" %(str(ex)))
                return 0                

            if negate:
                value = -value
                

            limit = pow(2,31)
            if value > limit-1:
                value = limit-1
            elif value < -limit:
                value = -limit
            
        return value # + new_str[i+len(first_string):]
