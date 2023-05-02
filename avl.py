'''
AVL tree
'''
from graphviz import Digraph
import html

class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 1 

    def __repr__(self):
        return '({}) | height: {}'.format(self.data, self.height)
        


class AvlTree:

    def __init__(self):
        self.root = None
        self.dot = Digraph(comment='AVL Tree', graph_attr={'rankdir':'TB', 'node_attr': {'shape': 'circle', 'width': '0.6'}, 'edge_attr': {'arrowsize': '0.8'}})
        self.node_counter = 0

    #FUNCTIONS USED TO VISUALIZE TREES

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
        dot.render('avl', view=True)

    def _display_helper(self, current, dot):
        if current is not None:
            dot.node(str(current.data), label=str(html.escape(str(current.data))))
            if current.left_child is not None:
                dot.edge(str(current.data), str(current.left_child.data))
                self._display_helper(current.left_child, dot)
            if current.right_child is not None:
                dot.edge(str(current.data), str(current.right_child.data))
                self._display_helper(current.right_child, dot)

    #ends Visualization
    '''
    def insert(self, value: int):

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        

    def _insert(self, value: int, subtree: Node):

        if value < subtree.data: #left
            if subtree.left_child is None:
                subtree.left_child = Node(value)
                subtree.left_child.parent = subtree #setting parent to previous node
                self._inspect_insertion(subtree.left_child)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data: #right
            if subtree.right_child is None:
                subtree.right_child = Node(value)
                subtree.right_child.parent = subtree
                self._inspect_insertion(subtree.right_child)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    #HEIGHT    
        
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        
        else:
            return 0
        

    def _height(self,subtree: Node, current_height:int):

        if subtree==None: return current_height

        left_height = self._height(subtree.left_child,current_height+1)
        right_height= self._height(subtree.right_child,current_height+1)
        
        return max(left_height,right_height)
  
    #end HEIGHT

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
 
    def find(self,value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None
   
    def _find(self, value, subtree: Node):
        if value == subtree.data:
            return subtree
        elif value < subtree.data and subtree.left_child!=None:
            return self._find(value, subtree.left_child)
        elif value > subtree.data and subtree.right_child != None:
            return self._find(value, subtree.right_child)


    def delete_value(self,value):
            
        return self.delete_node(self.find(value))

    def delete_node(self, node:Node):
        
        if node == None or self.find(node.data)==None:
            print("Node not found!")
            return None
        
        def min_value_node(n: Node): #voy bajando en el tree por el lado izquierdo
            current = n
            while current.left_child!= None:
                current = current.left_child
            return current
        
        def num_children(n: Node):
            num_children = 0
            if n.left_child!= None: num_children+=1
            if n.right_child!= None: num_children+=1
            return num_children

        node_parent = Node()
        #node_parent = node.parent

        node_children =num_children(node)

        #1 OPTION (NO CHILDREN)
        if node_children == 0:

            if node_parent != None:
                if node_parent.left_child == node:
                    node_parent.left_child= None
                else:
                    node_parent.right_child=None
            else:
                self.root = None
        
        #2 OPTION (SINGLE CHILD)
        child= Node()
        if node_children == 1:
            
            
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            if node.parent != None:
                if node_parent.left_child == node:
                    node_parent.left_child = child
            else:
                self.root=child

        child.parent = node_parent
                
        #3 OPTION (TWO CHILDREN)
        if node_children==2:
            successor = min_value_node(node.right_child)

            #manteniendo en valor que vamos a eliminar
            node.data=successor.data
            self.delete_node(successor)

            return
        if node_parent != None:
            node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))
            self._inspect_delete(node_parent)
   
    #BALANCE FUNCTIONS

    def _inspect_insertion(self, subtree: Node, path =[]): #para que se usa path
        if subtree.parent==None: return
        path=[subtree]+path

        left_height =self.get_height(subtree.parent.left_child)
        right_height=self.get_height(subtree.parent.right_child)

        if abs(left_height-right_height)>1:
            path=[subtree.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return
        
        new_height = 1+subtree.height
        if new_height>subtree.parent.height:
            subtree.parent.height=new_height

        self._inspect_insertion(subtree.parent,path)



    def _inspect_delete(self, subtree: Node):
        if subtree == None: return
        left_height= self.get_height(subtree.left_child)
        right_height = self.get_height(subtree.right_child)

        if abs(left_height-right_height)>1:
            y= self._taller_child(subtree)
            x=self._taller_child(y)
            self._rebalance_node(subtree,y,x)

        self._inspect_delete(subtree.parent)

    def _rebalance_node(self, z: Node,y: Node,x: Node):
        if y==z.left_child and x==y.left_child:
            self._right_rotate(z)
        elif y==z.left_child and x==y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right_child and x==y.right_child:
            self._left_rotate(z)
        elif y==z.right_child and x==y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception("error en el calibrado")
        

    def _right_rotate(self,z: Node):
        #y= Node()
        sub_root= z.parent
        y= z.left_child
        t3 =y.right_child
        y.right_child = z
        z.parent=y
        if t3 != None: t3.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        
        z.height=1+max(self.get_height(z.left_child),self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))

    def _left_rotate(self,z: Node):
        sub_root=z.parent
        y=z.right_child
        t2=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=t2

        if t2 != None: t2.parent=z
        y.parent = sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.get_height(z.left_child),
			self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),
			self.get_height(y.right_child))
    

    def get_height(self, subtree: Node):
        if subtree == None: 
            return 0
        return subtree.height

    def _taller_child(self, subtree: Node):
        left=self.get_height(subtree.left_child)
        right=self.get_height(subtree.right_child)
        return subtree.left_child if left>=right else subtree.right_child
'''


    def insert(self, root, key):
	
		# Step 1 - Perform normal BST
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the
		# ancestor node
        root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
        balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)

		# Case 2 - Right Right
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)

		# Case 3 - Left Right
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

		# Case 4 - Right Left
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def leftRotate(self, z):
        
        y = z.right
        T2 = y.left

		# Perform rotation
        y.left = z
        z.right = T2

		# Update heights
        z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

		# Perform rotation
        y.right = z
        z.left = T3

		# Update heights
        z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
        return y
    
    def getHeight(self, root):
        if not root:
            return 0
        
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def preOrder(self, root):
        if not root:
            return
        
        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)