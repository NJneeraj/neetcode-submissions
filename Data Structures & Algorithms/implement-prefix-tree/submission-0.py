class TrieNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, s in enumerate(word):
            isEnd = i == len(word) - 1
            if s not in curr.children:
                curr.children[s] = TrieNode(isEnd)
            if isEnd:
                curr.children[s].isEnd = True
            curr = curr.children[s]

    def search(self, word: str) -> bool:
        curr = self.root
        for i,s in enumerate(word):
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
