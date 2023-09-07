# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/

class Trie:

    def __init__(self):
        self.char_dict = {}

    def insert_helper(self, current_trie, word, idx):
        if idx >= len(word):
            current_trie.char_dict['*'] = None
            return
        char = word[idx]
        if char not in current_trie.char_dict:
            current_trie.char_dict[char] = Trie()
        self.insert_helper(current_trie.char_dict[char], word, idx+1)

    def insert(self, word: str) -> None:
        self.insert_helper(self, word, 0)

    def search_helper(self, current_trie, word, idx, starts_with=False):
        if idx >= len(word):
            if starts_with:
                return True
            if '*' in current_trie.char_dict:
                return True
            return False
        if word[idx] not in current_trie.char_dict:
            return False
        return self.search_helper(current_trie.char_dict.get(word[idx]), word, idx+1, starts_with)


    def search(self, word: str) -> bool:
        return self.search_helper(self, word, 0)

    def startsWith(self, prefix: str) -> bool:
        return self.search_helper(self, prefix, 0, True) 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)