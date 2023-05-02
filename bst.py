'''
Binary Search Tree
'''
from graphviz import Digraph
import html


class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        return '({})'.format(self.data)
    

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.dot = Digraph(comment='Binary Search Tree', graph_attr={'rankdir':'TB', 'node_attr': {'shape': 'circle', 'width': '0.6'}, 'edge_attr': {'arrowsize': '0.8'}})
        self.node_counter = 0

        
    def add_node_to_the_graph(self, node):
        self.node_counter += 1
        self.dot.node(str(self.node_counter), str(node), shape="circle", style="filled", fillcolor="lightblue")

    def traverse_and_add_nodes_to_the_graph(self, subtree):
        if subtree is not None:
            self.add_node_to_the_graph(subtree.data)
            if subtree.left_child is not None:
                self.add_node_to_the_graph(subtree.left_child.data)
                self.dot.edge(str(subtree.data), str(subtree.left_child.data))
            if subtree.right_child is not None:
                self.add_node_to_the_graph(subtree.right_child.data)
                self.dot.edge(str(subtree.data), str(subtree.right_child.data))
            self.traverse_and_add_nodes_to_the_graph(subtree.left_child)
            self.traverse_and_add_nodes_to_the_graph(subtree.right_child)

    def display(self):
        dot = Digraph()
        self._display_helper(self.root, dot)
        dot.render('bst', view=True)

    def _display_helper(self, current, dot):
        if current is not None:
            dot.node(str(current.data), label=str(html.escape(str(current.data))))
            if current.left_child is not None:
                dot.edge(str(current.data), str(current.left_child.data))
                self._display_helper(current.left_child, dot)
            if current.right_child is not None:
                dot.edge(str(current.data), str(current.right_child.data))
                self._display_helper(current.right_child, dot)



    def insert(self, value: int):

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        
    def _insert(self, value: int, subtree: Node):

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    
    def traverse(self, subtree: Node):
        
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)


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
        

    def find_min(self, subtree: Node) -> int:

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree


    def find_max(self, subtree: Node) -> int:

        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree
    
    def delete(self, key: int):
        if self.root is None:
            return False
        else:
            self.root = self._delete(key, self.root)

    def _delete(self, key: int, subtree: Node):
        if subtree is None:
            return False
        
        if key < subtree.data:
            subtree.left_child = self._delete(key, subtree.left_child)
        elif key > subtree.data:
            subtree.right_child = self._delete(key, subtree.right_child)
        else:
            if subtree.left_child is None:
                temp = subtree.right_child
                subtree = None
                return temp
            elif subtree.right_child is None:
                temp = subtree.left_child
                subtree = None
                return temp
            temp = self.find_min(subtree.right_child)
            subtree.data = temp.data
            subtree.right_child = self._delete(temp.data, subtree.right_child)
        return subtree