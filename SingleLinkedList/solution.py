#class for creating nodes
class SingleNode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)

class SingleLinkedList:
    
    #initalizing head with none to initate the linked list with no argument
    def __init__(self):
        self.head = None

    def add_value(self,input_value):
        #checks if the current head is empty and create one with first input
        if self.head is None:
            self.head = SingleNode(input_value)
            return
        
        #our point takes the head value
        current_value = self.head

        #if the pointer has a node, set the current value to point to the node from the first
        while current_value.next is not None:
            current_value = current_value.next
        
        #initiate a new node that connects to an existing one in current
        current_value.next = SingleNode(input_value)
        
        #TODO: implement printing logic
