from node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.get_head() is None:
            self.head_node = new_node
            return

        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        temp.next_element = new_node
        return


    def isnsert_at_end_of_linked_list(self, data):
        while self.head_node == None:
            self.head_node = self.head_node.next_element
        
        temp_node = Node(data)
        self.head_node.next_element = temp_node


    def print_linked_list(self):
        while self.head_node != None:
            print(self.head_node.data)
            self.head_node = self.head_node.next_element


linkedlist = LinkedList()
linkedlist.insert_at_head(1)
linkedlist.insert_at_head(2)
linkedlist.insert_at_head(3)
linkedlist.insert_at_head(4)
linkedlist.print_linked_list()