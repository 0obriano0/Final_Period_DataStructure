#import random, math

outputdebug = False 

def debug(msg):
    if outputdebug:
        print(msg)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 
        self.database_ = None

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]:
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key, database_ = None):
        tree = self.node
        
        newnode = Node(key)
        newnode.database_ = database_
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key,database_)
            
        elif key > tree.key: 
            self.node.right.insert(key,database_)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 
    '''        
    def search(self,key):
        if self.node != None: 
            if self.node.key == key: 
                return  self.node.database_
            elif key < self.node.key: 
                return self.node.left.search(key)  
            elif key > self.node.key: 
                return self.node.right.search(key)
        else: 
            return None
    '''
        
    def search(self,*args):
        a = 1
        if len(args) == 1 and type(args[0]) == type(a):
            key = args[0]
            if self.node != None:
                if self.node.key == key: 
                    return  self.node.database_
                elif key < self.node.key: 
                    return self.node.left.search(key)  
                elif key > self.node.key: 
                    return self.node.right.search(key)    
        elif len(args) == 2:
            key = args[0]
            vaule = args[1]
            final_list = []
            if self.node != None:
                if self.node.database_.search(key) == vaule:
                    final_list.append(self.node.database_)
                
                l = self.node.left.search(key,vaule)
                if l is not None:
                    for data in l:
                        final_list.append(data)
                
                l = self.node.right.search(key,vaule)
                if l is not None:
                    for data in l:
                        final_list.append(data)
                return final_list
        return None
    
    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.key == key: 
                debug("Deleting ... " + str(key))  
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check 
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))  
                        self.node.key = replacement.key 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.key)
                    
                self.rebalance()
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
                        
            self.rebalance()
        else: 
            return 

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if(self.node != None): 
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '  )  
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')
    
    def get_all(self,):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.get_all()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.database_)

        l = self.node.right.get_all()
        for i in l: 
            inlist.append(i) 
    
        return inlist 
    
    def show(self,):
        for data in self.get_all():
            print(data.RN," = ",data.name)

# Usage example
if __name__ == "__main__": 
    import database
    '''
    a = AVLTree()
    print("----- Inserting -------")
    #inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in inlist: 
        a.insert(i)
         
    a.display()
    
    print("----- Deleting -------")
    a.delete(3)
    a.delete(4)
    # a.delete(5) 
    a.display()

    print 
    print("Input            :", inlist )
    print("deleting ...       ", 3)
    print("deleting ...       ", 4)
    print("Inorder traversal:", a.inorder_traverse() )
    '''
    print("---------------------------分隔線---------------------------")
    b = AVLTree()
    data_dict_translat = {}
    b.insert(50,database.vendor("廠商一","123456789"))
    data_dict_translat["廠商一"] = 50
    
    b.insert(40,database.vendor("廠商二","4455544"))
    data_dict_translat["廠商二"] = 40
    
    b.insert(60,database.vendor("廠商三","44466644"))
    data_dict_translat["廠商三"] = 60
    
    b.insert(30,database.vendor("廠商四","448844"))
    data_dict_translat["廠商四"] = 30
    
    b.insert(-10,database.vendor("廠商五","4488944"))
    data_dict_translat["廠商五"] = -10
    
    b.insert(70,database.vendor("廠商六","4449994"))
    data_dict_translat["廠商六"] = 70
    
    b.insert(35,database.vendor("廠商七","4488844"))
    data_dict_translat["廠商七"] = 35
    
    b.insert(36,database.vendor("廠商八","123456"))
    data_dict_translat["廠商八"] = 36
    
    b.insert(11222,database.vendor("廠商八","1234567"))
    data_dict_translat["廠商八"] = 11222
    
    b.insert(1122232,database.vendor("廠商八","12345678"))
    data_dict_translat["廠商八"] = 1122232
    
    b.insert(34444,database.vendor("廠商八","123456789"))
    data_dict_translat["廠商八"] = 34444
    
    b.insert(38,database.vendor("廠商九","448899944"))
    data_dict_translat["廠商九"] = 38
    
    b.display()
    print(b.search(50).name)
    print(b.search(40).name)
    print(b.search(60).name)
    print(b.search(30).name)
    print(b.search(-10).name)
    print(b.search(70).name)
    print(b.search(35).name)
    print(b.search(36).name)
    print(b.search(38).name)
    
    print(b.inorder_traverse())
    
    print("\n---------------------------分隔線---------------------------")
    b.delete(70)
    if b.search(70) is not None:
        print(b.search(70).name)
    else:
        print("找不到 70")
    b.display()
    print(b.inorder_traverse())
    b.show()
    abcdefg = []
    abcdefg = b.get_all()
    
    for data in b.search('name','廠商八'):
        print(data.name, " = ", data.RN)