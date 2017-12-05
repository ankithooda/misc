class Node:
    def __init__(self, data, next_node, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        print("Self          : ", self.data)
        if self.prev_node != None:
            print("Previous Node : ", self.prev_node.get_data())
        if self.next_node != None:
            print("Next Node     : ", self.next_node.get_data())
        return str("")   

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node
        
    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, node):
        self.prev_node = node
        
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
