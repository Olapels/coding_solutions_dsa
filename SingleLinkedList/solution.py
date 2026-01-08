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

        #checks if the current head is empty and create one with first input, next will be empty for now
        if self.head is None:
            self.head = SingleNode(input_value)
            return
        
        #current value is initiated with the first input
        current_value = self.head

        #current_value.next can only be empty if there is no new input
        while current_value.next is not None:
            current_value = current_value.next
        
        #the next input value is set as current_value.next effectively creating a link
        current_value.next = SingleNode(input_value)
    
    def print_nodes(self):

        #if head is empty -- no input yet
        if not self.head:
            print("empty linked list")
            return
        
        nodes_list = []
        current_value = self.head

        while current_value:
            nodes_list.append(current_value.value)
            #set current value to the next, moving pointer one step forward
            current_value = current_value.next
        
        print ("-->".join(nodes_list))
