class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]

        cur.isEnd = True

    def search(self, word: str, cur=None) -> bool:

        if cur is None:
            cur = self.root

        for i, c in enumerate(word):
            if c == '.':
                for child in cur.children.values():
                    if self.search(word[i + 1:], child):
                        return True
                return False
            
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.isEnd

    