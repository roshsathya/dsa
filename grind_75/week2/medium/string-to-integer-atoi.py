# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:

    def convert_string_to_number(self, string_list):
        total_len = len(string_list) - 1
        output = 0
        for value in string_list:
            if total_len == 0:
                output += value
            else:
                output += value * (10**total_len)
            total_len -= 1
        return output


    def myAtoi(self, s: str) -> int:
        idx = 0
        output = []
        is_positive = True
        s = s.lstrip()

        while idx < len(s):
            if s[idx] == "-" or s[idx] == "+":
                if idx != 0:
                    break
                if s[idx] == "-":
                    is_positive = False
                idx += 1
                continue
            
            number = None
            try:
                number = int(s[idx])
            except:
                break

            if number == 0 and not output:
                idx += 1
                continue
            output.append(number)
            idx += 1

        if not output:
            return 0

        final_number = self.convert_string_to_number(output)
        if not is_positive:
            final_number *= -1
        if final_number < -2**31:
            return -2**31
        if final_number > 2**31 - 1:
            return 2**31 - 1
            
        return final_number