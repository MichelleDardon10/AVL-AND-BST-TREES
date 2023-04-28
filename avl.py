'''
AVL tree
'''

class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 0 

    def __repr__(self):
        return '({}) | height: {}'.format(self.data, self.height)
        #VISUALIZATION 


class AvlTree:

    def __init__(self):

        self.root = None


    
    def insert(self, value: int):

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        

    def _insert(self, value: int, subtree: Node):

        if value < subtree.data: #izquierda
            if subtree.left_child is None:
                subtree.left_child = Node(value)
                subtree.left_child.parent = subtree
                #self._inspect_insertion(subtree.left_child)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data: #derecha
            if subtree.right_child is None:
                subtree.right_child = Node(value)
                subtree.right_child.parent = subtree
                #self._inspect_insertion(subtree.right_child)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    #print_tree    
        
    def height1(self):
        if self.root != None:
            return self._height1(self.root,0)
        
        else:
            return 0
        

    def _height1(self,subtree: Node, current_height:int):

        if subtree==None: return current_height

        left_height = self._height1(subtree.left_child,current_height+1)
        right_height= self._height1(subtree.right_child,current_height+1)
        
        return max(left_height,right_height)

    def get_height(self, subtree: Node):
        if subtree == None: 
            return 0
        return subtree.height
        

    def traverse(self, subtree: Node):
        
        print(subtree)


        if subtree.left_child is not None:
            self.traverse(subtree.left_child)
            self.get_height
        if subtree.right_child is not None:
            self.traverse(subtree.right_child)
            self.get_height
        

    
    def find_min(self, subtree: Node) -> int:

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree



    def find_max(self, subtree: Node) -> int:

        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree
    

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