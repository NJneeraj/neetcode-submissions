class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            for i in range(j, len(word)):
                s = word[i]
                if s == ".":
                    for child in node.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if s not in node.children:
                        return False
                    node = node.children[s]
            return node.isEnd

        return dfs(self.root, 0)
