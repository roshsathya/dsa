class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        char_dict = {}
        window_size = len(p)
        total_chars = 0
        output = []

        for char in p:
            if char not in char_dict:
                char_dict[char] = 0
                total_chars += 1
            char_dict[char] += 1

        for idx in range(window_size):
            if s[idx] not in char_dict:
                continue
            char_dict[s[idx]] -= 1
            if char_dict[s[idx]] == 0:
                total_chars -= 1
            
        idx = 0
        while idx < len(s)-window_size:
            if total_chars == 0:
                output.append(idx)

            if s[idx] in char_dict:
                char_dict[s[idx]] += 1
                if char_dict[s[idx]] == 1:
                    total_chars += 1
            
            if s[idx+window_size] in char_dict:
                char_dict[s[idx+window_size]] -= 1
                if char_dict[s[idx+window_size]] == 0:
                    total_chars -= 1

            idx += 1

        if total_chars == 0:
            output.append(idx)

        return output 
        