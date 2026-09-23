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
        curr = self.root

        def searchDFS(node, word):
            for i, s in enumerate(word):
                if s == ".":
                    char = None
                    for w in node.children.keys():
                        if searchDFS(node.children[w], word[i + 1 :]):
                            char = w
                            break
                    if char:
                        node = node.children[char]
                    else:
                        return False
                else:
                    if s not in node.children:
                        return False
                    node = node.children[s]
            return node.isEnd

        return searchDFS(curr, word)
