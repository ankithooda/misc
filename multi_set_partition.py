def create_interleave_list(set_list, n):
    """
    Takes a list of list of symbols and create another list with symbols interleaved from each set.
    """
    interleaved_list = []
    for i in range(0, n):
        for single_set in set_list:
            interleaved_list.append(single_set[i])
    return interleaved_list

def swap_elements(list_1, source_index, dest_index):
    """
    Swaps the element at dest_index with source_index when source_index is greater. 
    """
    if source_index != dest_index:
        temp = list_1[source_index]
        list_1[source_index] = list_1[dest_index]
        list_1[dest_index] = temp        

def shift_insert(list_1, source_index, dest_index):
    """
    Swaps the element at dest_index with source_index when source_index is greater. Does not change the relative order.
    """
    if source_index > dest_index:
        for i in range(dest_index, source_index + 1):
            swap_elements(list_1, i, source_index)

def single_set_partition(input_list, set_1, partition_index):
    """
    Accumulates the symbols belonging to the set_1 at the partition_index without changing the relative order
    of neither the symbols belonging to set_1 or nor of those not belonging to set_1.
    """
    for iter_index in range(0, len(input_list)):
        if input_list[iter_index] in set_1:
            shift_insert(input_list, iter_index, partition_index)
            partition_index = partition_index + 1
    return partition_index

def multi_set_partition(input_list, set_list):
    """
    Takes an input_list comprising of symbols.
    Takes a list of lists of symbols.
    Reorders the input list so that symbols belonging to one set are accumulated together without changing
    the origial order of symbols within a set.
    Complexity -> m * n * n (Where m is the number of sets and n is the length of the input list)    
    """
    current_partition_index = 0
    for single_set in set_list:
        current_set_partition = single_set_partition(input_list, single_set, current_partition_index)    
    
## Testing Boilerplate ##
set_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
set_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
set_3 = ['x', 'y', 'z', 'xx', 'yy', 'zz', 'qq', 'vv', 'ww']
set_4 = [100, 200, 300, 400, 500, 600, 700, 800, 900]

set_list = [set_1, set_2, set_3, set_4]
input_list = create_interleave_list(set_list, 9)

print("List of Lists of Symbols - ", set_list)
print("Sample Input  - ", input_list)
multi_set_partition(input_list, set_list)
print("Sample Output - ", input_list)


