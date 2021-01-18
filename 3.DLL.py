class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
  
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
            if self.start_node is None:
                new_node = Node(data)
                self.start_node = new_node
            else:
                print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def traverse_list(self):
            if self.start_node is None:
                print("List has no element")
                return
            else:
                n = self.start_node
                while n is not None:
                    print(n.item)
                    n = n.nref

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def search_item(self, x):
            if self.start_node is None:
                print("List has no elements")
                return
            n = self.start_node
            while n is not None:
                if n.item == x:
                    print(x," Item found")
                    return True
                n = n.nref
            print(x," item not found")
            return False

    def find_element_at(self, x):
        count =1 
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if count == x:
                print(n.item," Item found at position ",x)
                return True
            n = n.nref
            count=count+1
        print(x," item not found")
        return False

    def largestElement(self):   
        max = -32767
        n=self.start_node  
     
        while n is not None:
          if (max < n.item) : 
                max = n.item  
          n = n.nref
          
        return max
      
    def smallestElement(self):  
        min = 32767
        n=self.start_node 
        while n is not None:  
            if (min > n.item) : 
                min = n.item  
            n = n.nref   
        return min

    def list_sucessor(self,x):
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Succesor of",x,"is", n.nref.item)
            n = n.nref

    def list_predecessor(self,x):
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Predecesor of",x,"is", n.pref.item)
            n = n.nref

    def deleteList(self):
        n = self.start_node
        while n is not None:
            print("Deleting Element : ",n.item)
            del n.item
            n = n.nref

    def merge(self, first, second): 
      if first is None: 
        return second  
      if second is None: 
        return first 
      if first.item < second.item: 
        first.nref = self.merge(first.nref, second) 
        first.nref.pref = first 
        first.pref = None
        return first 
      else: 
        second.nref = self.merge(first, second.nref) 
        second.nref.pref = second 
        second.pref = None
        return second 

    def mergeSort(self, tempHead): 
      if tempHead is None: 
        return tempHead 
      if tempHead.nref is None: 
        return tempHead 
      second = self.split(tempHead) 
      tempHead = self.mergeSort(tempHead) 
      second = self.mergeSort(second) 
      return self.merge(tempHead, second) 

    def split(self, tempHead): 
      fast = slow = tempHead 
      while(True): 
        if fast.nref is None: 
          break
        if fast.nref.nref is None: 
          break
        fast = fast.nref.nref
        slow = slow.nref    
      temp = slow.nref
      slow.nref = None
      return temp 

    def push(self, new_data): 
      new_node = Node(new_data) 
      new_node.nref = self.start_node  
      if self.start_node is not None: 
        self.start_node.pref= new_node 
      self.start_node = new_node 

    def printList(self, node): 
      temp = node 
      print("Forward Traversal using nref poitner")
      while(node is not None): 
        print(node.item,end = " ")
        temp = node 
        node = node.nref
      print ("\nBackward Traversal using pref pointer")
      while(temp): 
        print (temp.item,end = " ") 
        temp = temp.pref
    
dll=DoublyLinkedList()
print("DOUBLY LINKED LIST")
print ("Inserting in the beginning ")
dll.insert_in_emptylist(5)
dll.insert_at_start(1)
dll.insert_at_start(88)
dll.insert_at_start(98)
dll.traverse_list()
print ("Inserting at the end ")
dll.insert_at_end(22)
dll.insert_at_end(74)
dll.insert_at_end(51)
dll.traverse_list()
print ("Inserting in Between")
dll.insert_after_item(5, 42)
dll.insert_before_item(22, 10)
dll.traverse_list()
print ("Deleting at start")
dll.delete_at_start()
dll.traverse_list()
print ("Delete at the end")
dll.delete_at_end()
dll.traverse_list()
print ("Delete by value")
dll.delete_element_by_value(5)
dll.traverse_list()
dll.push(5) 
dll.push(20) 
dll.push(4) 
dll.push(3) 
dll.push(30)
#Merge Sort
print("Original Linked List ")
dll.traverse_list()
dll.start_node = dll.mergeSort(dll.start_node) 
print("Linked List after sorting")
dll.printList(dll.start_node) 
print ("\nSearching") 
dll.search_item(30)
dll.search_item(51)
dll.find_element_at(2)
print("The Largest Element is " ,dll.largestElement())
print("The Smallest Element is " ,dll.smallestElement())
print("Printing sucessor ")
dll.list_sucessor(30)
print ("Printing predecessor ")
dll.list_predecessor(4)
print ("Deleting Entire List :")
dll.deleteList()