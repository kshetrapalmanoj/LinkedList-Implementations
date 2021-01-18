class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class CircularLinkedList:   
    def __init__(self):    
        self.head = None;    
        self.tail = None;  
        self.size = 0;     

    def display(self):     
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        while(current != None):      
            print(current.data)    
            current = current.next

    def addAtEnd(self, data):       
        newNode = Node(data);      
        if(self.head == None):       
            self.head = self.tail = newNode;       
            self.head.previous = None;       
            self.tail.next = None;     
        else:      
            self.tail.next = newNode;      
            newNode.previous = self.tail;        
            self.tail = newNode;      
            self.tail.next = None;      

    def addAtStart(self, data):      
        newNode = Node(data);        
        if(self.head == None):      
            self.head = self.tail = newNode;       
            self.head.previous = None;     
            self.tail.next = None;      
        else:      
            self.head.previous = newNode;       
            newNode.next = self.head;     
            newNode.previous = None;      
            self.head = newNode;  

    def insert_after_item(self, x, data):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node           

    def deleteFromEnd(self):    
        if(self.head == None):    
            return;    
        else:     
            if(self.head != self.tail):      
                self.tail = self.tail.previous;      
                self.tail.next = None;   
            else:    
                self.head = self.tail = None;   

    def deleteFromStart(self):    
        if(self.head == None):    
            return;    
        else:    
            if(self.head != self.tail):    
                self.head = self.head.next;     
                self.head.previous = None;    
            else:    
                self.head = self.tail = None;     

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print(x,"item not found in the list")
        else:
            n.next = n.next.next            
      
    def append(self, new_value): 
        new_node = Node(new_value) 
        if self.head is None: 
            self.head = new_node 
            return
        curr_node = self.head 
        while curr_node.next is not None: 
            curr_node = curr_node.next
        curr_node.next = new_node     

    def sortedMerge(self, a, b): 
        result = None
        if a == None: 
            return b 
        if b == None: 
            return a 
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result   

    def mergeSort(self, h): 
         
        if h == None or h.next == None: 
            return h  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h) 
        right = self.mergeSort(nexttomiddle)   
        sortedlist = self.sortedMerge(left, right) 

        return sortedlist 
    def getMiddle(self, head): 
        if (head == None): 
            return head 
        slow = head 
        fast = head 
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
        return slow 

    def search_item(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                print(x," Item found")
                return True
            n = n.next
        print(x," item not found")
        return False

    def find_element_at(self, x):
        count =1 
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if count == x:
                print(n.data,"Item found at position ",x)
                return True
            n = n.next
            count=count+1
        print(x,"item not found")
        return False

    def largestElement(self):   
        max = -32767
        n=self.head  
        while n is not None:
          if (max < n.data) : 
                max = n.data 
          n = n.next   
        return max

    def smallestElement(self):  
        min = 32767
        n=self.head
        while n is not None: 
            if (min > n.data) : 
                min = n.data  
            n = n.next      
        return min

    def list_sucessor(self,x):
        n = self.head
        while n is not None:
            if n.data == x:
                print("Succesor of",x,"is", n.next.data)
            n = n.next

    def list_predecessor(self,x):
        n = self.head
        while n is not None:
            if n.next.data == x:
                print("Predecesor of",x,"is", n.data)
                break
            n = n.next

    def deleteList(self):
        n = self.head
        while n is not None:
            print("Deleting Element : ",n.data)
            del n.data
            n = n.next  

def printList(head): 
    if head is None: 
        print(' ') 
        return
    curr_node = head 
    while curr_node: 
        print(curr_node.data, end = " ") 
        curr_node = curr_node.next
    print(' ') 
            
dList = CircularLinkedList(); 
print("CIRCULAR LINKED LIST")
print("Inserting at the end")     
dList.addAtEnd(2)         
dList.addAtEnd(3)     
dList.addAtEnd(5)      
dList.addAtEnd(10)       
dList.addAtEnd(15)    
dList.display()
print("Inserting at the start") 
dList.addAtStart(6)  
dList.addAtStart(7) 
dList.addAtStart(8)    
dList.addAtStart(9)     
dList.display()   
print("Inserting in between two elements")  
dList.insert_after_item(10,22)
print("The linked list is :")
dList.display() 
print("Delete at the end")
while(dList.head != None):    
    dList.deleteFromEnd();    
    print("Updated List: ")    
    dList.display()
dList.addAtEnd(2)         
dList.addAtEnd(3)     
dList.addAtEnd(5)       
dList.addAtEnd(10)        
dList.addAtEnd(15) 
dList.display()
print("Delete at the start")
while(dList.head != None):    
    dList.deleteFromStart()     
    print("Updated List: ")  
    dList.display()
dList.addAtStart(6) 
dList.addAtStart(7)
dList.addAtStart(8)   
dList.addAtStart(9)     
print("Delete a value")
dList.delete_element_by_value(7)
dList.display();
print("Delete a value")
dList.delete_element_by_value(8)
dList.display()
print("The linked list is :")
dList.display()   
    # The list shall be: 2->3->20->5->10->15  
dList.append(15)
dList.append(10) 
dList.append(5)
dList.append(20)
dList.append(3)
dList.append(2)
print("Original Linked List is:")
dList.display()
  # Apply merge Sort  
dList.head = dList.mergeSort(dList.head) 
print ("Sorted Linked List is:") 
printList(dList.head)
print("Search element by Data given " )      
dList.search_item(2)  
dList.search_item(4)
print("Search element at a position ")  
dList.find_element_at(3)
print("The Largest Element is:" ,dList.largestElement())
print("The Smallest Element is:" ,dList.smallestElement())
print("Printing sucessor:")
dList.list_sucessor(10)
print("Printing predecessor:")
dList.list_predecessor(3)