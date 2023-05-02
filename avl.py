from graphviz import Digraph
class Node:

    def __init__(self, data: int) -> None:     
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0
        self.balance_factor = 0
    
    def __repr__(self):
        return '({}) | height: {}'.format(self.data, self.height)


class AVLTree:  

    def __init__(self):
        self.root = None


    def to_graphviz(self):
        dot = Digraph(comment='AVL Tree')
        self._to_graphviz(dot, self.root)
        return dot


    def _to_graphviz(self, dot, node):
        if node is None:
            return

        dot.node(str(node.data), str(node.data))
        if node.left_child is not None:
            dot.edge(str(node.data), str(node.left_child.data))
            self._to_graphviz(dot, node.left_child)

        if node.right_child is not None:
            dot.edge(str(node.data), str(node.right_child.data))
            self._to_graphviz(dot, node.right_child)


    def get_height(self, node: Node):
        if node is None:
            return -1
        else:
            return node.height


    def get_balance_factor(self, node: Node):
        if node is None:
            return 0
        else:
            return (self.get_height(node.left_child) - self.get_height(node.right_child))


    def update_height_and_balance_factor(self, node: Node):
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        node.balance_factor = self.get_balance_factor(node)


    def rotate_left(self, node: Node):
        new_parent = node.right_child
        node.right_child = new_parent.left_child
        new_parent.left_child = node

        self.update_height_and_balance_factor(node)
        self.update_height_and_balance_factor(new_parent)

        return new_parent


    def rotate_right(self, node: Node):
        new_parent = node.left_child
        node.left_child = new_parent.right_child
        new_parent.right_child = node

        self.update_height_and_balance_factor(node)
        self.update_height_and_balance_factor(new_parent)

        return new_parent


    def rotate_left_right(self, node: Node):
        node.left_child = self.rotate_left(node.left_child)
        return self.rotate_right(node)


    def rotate_right_left(self, node: Node):
        node.right_child = self.rotate_right(node.right_child)
        return self.rotate_left(node)
    

    def find_max(self, subtree: Node) -> int:

        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree


    def insert(self, value: int):

        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(value, self.root)

    def _insert(self, value: int, node: Node):
        if value < node.data:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                node.left_child = self._insert(value, node.left_child)

            if self.get_balance_factor(node) > 1:
                if self.get_balance_factor(node.left_child) < 0:
                    node = self.rotate_left_right(node)
                else:
                    node = self.rotate_right(node)

        elif value > node.data:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                node.right_child = self._insert(value, node.right_child)

            if self.get_balance_factor(node) < -1:
                if self.get_balance_factor(node.right_child) > 0:
                    node = self.rotate_right_left(node)
                else:
                    node = self.rotate_left(node)

        self.update_height_and_balance_factor(node)

        return node

    def search(self, key: int) -> bool:

        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:

        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False

    def traverse(self, subtree: Node):
        
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)

    
    def find_min(self, subtree: Node) -> int:

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree        
    
    
    def delete(self, value: int) -> None:
        self.root = self._delete(value, self.root)


    def _delete(self, value: int, node: Node):
        if node is None:
            return node

        if value < node.data:
            node.left_child = self._delete(value, node.left_child)
        elif value > node.data:
            node.right_child = self._delete(value, node.right_child)
        else:

            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            else:
                successor_node = node.right_child
                while successor_node.left_child is not None:
                    successor_node = successor_node.left_child

                node.data = successor_node.data

                node.right_child = self._delete(successor_node.data, node.right_child)

        self.update_height_and_balance_factor(node)

        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1:
            if self.get_balance_factor(node.left_child) < 0:
                node = self.rotate_left_right(node)
            else:
                node = self.rotate_right(node)
        elif balance_factor < -1:
            if self.get_balance_factor(node.right_child) > 0:
                node = self.rotate_right_left(node)
            else:
                node = self.rotate_left(node)

        return node