class Trie:

    def __init__(self) -> None:
        self._root = Node()



    def insert(self, string: str) -> bool:
        """
        """
        depth = len(string)
        current = self._root
        changed = False

        for i in range(depth):
            if string[i] not in current.children:
                current.children[string[i]] = Node()
                changed = True
            current = current.children[string[i]]

        current.terminal = True
        return changed



    def is_empty(self) -> bool:
        """
        """
        return len(self._root) == 0

        

    def delete(self, string: str) -> None:
        """
        NOT TESTED YET
        """
        def __delete(self, root: Optional[Node], string: str, depth: int) -> Optional[Node]:
            """
            """
            if root is None:
                return None

            if depth == len(string):

                if root.terminal:
                    root.terminal = False

                if len(root) == 0:
                    return None

                return root

            root.children[string[depth]] = __delete(root.children[string[depth]],
                                                    string, depth + 1)
            if len(root) == 0 and not root.terminal:
                root = None

            return root

        __delete(self._root, string, 0)



    def contains(self, string: str) -> bool:
        """
        """
        depth = len(string)
        current = self._root

        for i in range(depth):
            if string[i] not in current.children:
                return False
            current = current.children[string[i]]

        return current.terminal



    class Node:
        def __init__(self) -> None:
            self.terminal = False
            self.children = dict()