class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isEnd = True


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        curr = self.root
        for word in words:
            curr.addWord(word)
        res, visited = set(), set()
        ROW, COL = len(board), len(board[0])

        def dfs(node, row, col, word):
            if (
                (row, col) in visited
                or row < 0
                or col < 0
                or row == ROW
                or col == COL
                or board[row][col] not in node.children
            ):
                return
            c = board[row][col]
            visited.add((row, col))
            node = node.children[c]
            word += c
            if node.isEnd:
                res.add(word)
            dfs(node, row + 1, col, word)
            dfs(node, row - 1, col, word)
            dfs(node, row, col + 1, word)
            dfs(node, row, col - 1, word)
            visited.remove((row, col))
        for r in  range(ROW):
            for c in range(COL):
                dfs(curr,r,c,"")
       
        return list(res)
