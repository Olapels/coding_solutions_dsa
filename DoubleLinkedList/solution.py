
class DoublelinkedListNode:

    def __init__(self,value,previous_node=None,next_node=None)-> None:
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node
    
    def __str__(self)-> str:
        return str(self.value)


class DoubleNodelinking:

    def __init__(self) -> None:
        self.head  = None
        self.tail = None

    def node_linking(self,input_value)-> None:
        if not input_value:
            raise InterruptedError("Expected an input")
        
        new_node = DoublelinkedListNode(input_value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        
    def print_nodes(self) -> str:

        if self.head is None:
            return "Empty list"
        
        identifier = self.tail
        linked_list = []

        while identifier is not None:
            linked_list.append(str(identifier.value))
        
            identifier  = identifier.previous_node  
        

        print('<--'.join(linked_list))



