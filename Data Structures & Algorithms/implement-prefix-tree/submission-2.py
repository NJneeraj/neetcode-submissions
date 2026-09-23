class TrieNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True
