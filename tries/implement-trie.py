class Trie(object):
    def __init__(self):
        self.root =  TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.characters:
                node.characters[char] = TrieNode(char)
            node = node.characters[char]
        node.is_word = True
        

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.characters: return False
            node = node.characters[char]
        
        if(node.is_word == True): return True
        else: return False
        

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.characters: return False
            node = node.characters[char]
        
        return True

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.characters = {}
        self.is_word = False


# Your Trie object will be instantiated and called as such:

obj = Trie()
print("None")
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))
"""
obj = Trie()
print("None")
print(obj.insert("a"))
print(obj.search("a"))
print(obj.startsWith("a"))
"""
