# This module consists of common linked list algorithms and methods.
# The implementation of the algorithms is independent of the undelying implementation of the linked list node.
# The algorithm expects each node in the linked list to have the following methods defined.
# Create a new node.
# Get the next pointer - get_next_node().
# Set the next pointer - set_next_node().
# Get the previous pointer - get_prev_node().
# Set the previous pointer - set_next_node().
# Get the data - get_data().
# Set the data - set_data().

def count(head):
    """
    Returns the counts elements in the list.    
    """
    if head != None:
        return 1 + count(head.get_next_node())
    else:
        return 0

def nth(head, n):
    """
    Returns the nth element in the list otherwise None
    """
    if head == None:
        return None
    elif n == 0:
        return head
    else:
        return nth(head.get_next_node(), n-1)

def pop(head):
    """
    head : Head of the link
    Returns a tuple consisting of (old head, new head).
    """
    if head == None:
        return (None, None)
    else:
        new_head = head.get_next_node()
        head.set_next_node(None)
        return (head, new_head)

def insert_nth(head, n, node):
    """
    Insert a new node at the n position in the linked list.
    If n is greater than the list's length then nothing happens. This can be fixed to add new element at the end of list.
    """
    if head == None and n != 0:
        return None
    elif n == 0:
        node.set_next_node(head)
        return node
    else:
        head.set_next_node(insert_nth(head.get_next_node(), n - 1, node))
        return head

def sorted_insert(head, node):
    """
    Given a sorted linked list, insert a new node is the correct place.
    """
    if head == None or head.get_next_node() == None:
        return node
    elif head.get_data() >= node.get_data():
        node.set_next_node(head)
        return node
    else:
        head.set_next_node(sorted_insert(head.get_next_node(), node))
        return head

def sort(head):
    """
    Sort the linked list.
    """
    pass

def append(list1, list2):
    """
    Appends list2 at the end of list1. Mutates list1, return nothing. NON FUNCTIONAL.
    """
    if list1.get_next_node() == None:
        list1.set_next_node(list2)
    else:
        append(list1.get_next_node(), list2)        

def front_back_split(list1):
    """
    Splits the list1 down the middle with odd element going in the front list.
    Returns a tuple of two lists.
    """
    list_length = count(list1)
    split_element = nth(list1, round(list_length/2) - 1)
    first_list = list1
    last_list = split_element.get_next_node()
    split_element.set_next_node(None)
    return (first_list, last_list)

def remove_duplicates(list1):
    """
    Remove duplicates from a sorted linked list.
    """
    if list1 != None and list1.get_next_node() != None:
        if list1.get_data() == list1.get_next_node().get_data():
            return remove_duplicates(list1.get_next_node())
        else:
            list1.set_next_node(remove_duplicates(list1.get_next_node()))
            return list1
    else:
        return list1
          
def print_list(head):
    """
    Prints the link list.
    """
    if head != None:
        print(head)
        print_list(head.get_next_node())
                    
####
#### Testing BoilerPlare
####

from node import Node
a = Node(600, None)
b = Node(600, a)
c = Node(500, b)
d = Node(200, c)
e = Node(200, d)
f = Node(100, e)
g = Node(100, f)

zz = Node(450, None)
xx = Node(550, zz)
yy = Node(650, xx)

print_list(remove_duplicates(g))
