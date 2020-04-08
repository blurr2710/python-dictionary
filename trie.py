class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        self.value = ""
class Trie:
    def __init__(self):
        self.root = Node()
    def initialize(self,t):
        t.add_word("apple")
        t.add_word("and")
        t.add_word("amigo")
        t.add_word("ant")
        t.add_word("asgard")
    def add_word(self, key):
        word_length = len(key)
        current = self.root
        for i in range(word_length):
            position = self.ord_char(key[i])

            if current.children[position] is None:
                current.children[position] = Node()
            current = current.children[position]
            current.value = key[i]
        current.end = True

    def ord_char(self,key):
        ord_rep = ord(key) - ord('a')
        return ord_rep
    def prefix_search(self, prefix):
        current = self.root
        # get to the starting point
        for c in prefix:
            current = current.children[self.ord_char(c)]
            if current is None:
                # prefix doesn't exist, abort with an empty list
                return []

        found = []
        stack = [(current, prefix)]
        while stack:
            current, prefix = stack.pop()

            if current.end:
                # this is a complete word, named by prefix
                found.append(prefix)

            # add the children to the stack, each with their letter added to the
            # prefix value.
            for child in current.children:
                if child is None:
                    continue
                stack.append((child, prefix + child.value))
        return found