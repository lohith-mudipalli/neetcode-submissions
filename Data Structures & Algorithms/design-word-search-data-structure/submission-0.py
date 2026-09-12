class TrieNode:
    def __init__(self):
        self.children ={}
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:

        current = self.root

        for i in word:

            if i not in current.children:
                current.children[i] = TrieNode()
            
            current = current.children[i]

        current.isEnd = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):

            if index == len(word):
                return node.isEnd

            char = word[index]

            if char != ".":

                if char not in node.children:
                    return False
                
                return dfs(index + 1, node.children[char])

            else:

                for child in node.children.values():

                    if dfs(index +1, child):
                        return True

                return False
        
        return dfs(0, self.root)
        
