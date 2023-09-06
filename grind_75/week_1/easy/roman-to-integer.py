# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        roman_dict = {
            'I': {
                "value": 1,
                "prev_element": None
            },
            "V": {
                "value" : 5,
                "prev_element": "I"
            },
            "X": {
                "value" :10,
                "prev_element": "I"
            },
            "L": {
                "value" : 50,
                "prev_element": "X"
            },
            "C": {
                "value" : 100,
                "prev_element": "X"
            },
            "D": {
                "value" : 500,
                "prev_element": "C"
            },
            "M": {
                "value" : 1000,
                "prev_element": "C"
            }
        }
        idx = 0
        while idx < len(s):
            current_char = s[idx]
            char_data = roman_dict[current_char]
            if idx > 0 and char_data['prev_element'] and s[idx-1] == char_data['prev_element']:
                count += char_data['value'] - roman_dict.get(char_data['prev_element'])["value"] - roman_dict.get(char_data['prev_element'])["value"]
            else:
                count += char_data['value']
            idx += 1
        return count