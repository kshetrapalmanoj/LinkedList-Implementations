class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head= new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node

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
            
    def search_item(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                print(x,"Item found")
                return True
            n = n.next
        print(x,"item not found")
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
        print(x," item not found")
        return False

    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return 
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return

        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return

        # Deleting first node 
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
   

    def largestElement(self):   
        max = -32767
        n=self.head
     
        while n is not None:
          if (max < n.data) : 
                max = n.data
          n = n.next
          
        return max
      
    def smallestElement(self):  
    # Declare a min variable and initialize  
    # it with INT_MAX value.  
    # INT_MAX is integer type and its value  
    # is 32767 or greater.  
        min = 32767
        n=self.head
         # Check loop while head not equal to None  
        while n is not None: 
          
            # If min is greater then head.data then  
            # assign value of head.data to min  
            # otherwise node point to next node.  
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
                print("Predecesor of ",x,"is", n.data)
                break
            n = n.next

    def deleteList(self):
        n = self.head
        while n is not None:
            print("Deleting Element : ",n.data)
            del n.data
            n = n.next
    def append(self, new_value): 
          
        # Allocate new node 
        new_node = Node(new_value) 
          
        # if head is None, initialize it to new node 
        if self.head is None: 
            self.head = new_node 
            return
        curr_node = self.head 
        while curr_node.next is not None: 
            curr_node = curr_node.next
              
        # Append the new node at the end 
        # of the linked list 
        curr_node.next = new_node 
          
    def sortedMerge(self, a, b): 
        result = None
          
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
              # pick either a or b and recur.. 
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result 
      
    def mergeSort(self, h):     
        # Base case if head is None 
        if h == None or h.next == None: 
            return h 
        # get the middle of the list  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
  
        # set the next of middle node to None 
        middle.next = None
  
        # Apply mergeSort on left list  
        left = self.mergeSort(h) 
          
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle) 
  
        # Merge the left and right lists  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist 
   
    # Utility function to get the middle  
    # of the linked list  
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
          
# Utility function to print the linked list  
def printList(head): 
    if head is None: 
        print(' ') 
        return
    curr_node = head 
    while curr_node: 
        print(curr_node.data, end = " ") 
        curr_node = curr_node.next
    print('  ')

new_linked_list = LinkedList()
print("SINGLY LINKED LIST")
print("Inserting at the end")
new_linked_list.insert_at_end(3)
new_linked_list.insert_at_end(12)
new_linked_list.insert_at_end(15)
new_linked_list.traverse_list()
print("Inserting at the start")
new_linked_list.insert_at_start(1)
new_linked_list.insert_at_start(99)
new_linked_list.insert_at_start(52)
new_linked_list.traverse_list()
print("Inserting Between : After an element ")
new_linked_list.insert_after_item(15,22)
print("The linked list is :")
new_linked_list.traverse_list()
print("Search element by Data given " )
new_linked_list.search_item(99)
new_linked_list.search_item(6)
print("Search element at a position ") 
new_linked_list.find_element_at(2)
print("Delete at the start")
new_linked_list.delete_at_start()
new_linked_list.traverse_list()
print("Delete at the end")
new_linked_list.delete_at_end()
new_linked_list.traverse_list()
print("Delete a value")
new_linked_list.delete_element_by_value(3)
new_linked_list.traverse_list()
print("Delete a value")
new_linked_list.delete_element_by_value(1)
new_linked_list.traverse_list()
print("The linked list is :")
new_linked_list.traverse_list()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
#Merge Sort
print("The original linked list is :")
new_linked_list.traverse_list()
new_linked_list.head = new_linked_list.mergeSort(new_linked_list.head) 
print ("Sorted Linked List is:") 
printList(new_linked_list.head)
print("The Largest Element is " ,new_linked_list.largestElement())
print("The Smallest Element is " ,new_linked_list.smallestElement())
print("Printing sucessor ")
new_linked_list.list_sucessor(10)
print("Printing predecessor ")
new_linked_list.list_predecessor(30)
print("Deleting entire Linked List")
new_linked_list.deleteList()