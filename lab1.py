def max_list_iter(int_list): 
    """checks if list is empty"""
    if int_list == []:
        return None
    """checks if list is None"""
    if int_list == None:
        raise ValueError('List is None')
    else:
        """sets max_int to first term of list"""
        max_int = int_list[0]
        """compares max_int to every other term, replacing max_int with any number higher"""
        for i in range(len(int_list)):
            if int_list[i] > max_int:
                max_int = int_list[i]
        return max_int

def reverse_rec(int_list):
    """checks if list is None"""
    if int_list == None:
        raise ValueError("list is None")  
    """Base Case: returns empty list when length is 0"""     
    if len(int_list) == 0:
        return []
    """returns last element of list + recursively calls list with last index taken out"""
    return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list): 
    """Checks if list is None"""
    if int_list == None:
        raise ValueError("List is None")
    """Checks if list is empty"""
    if len(int_list) == 0:
        return None
    """checks if mid is target"""
    if int_list[high//2] == target:
        return target
    """if target is lower than mid, then recursively calls with same target, same low, new high, and new list from low to mid+1"""
    if int_list[high//2] > target:
        return bin_search(target, 0, high//2, int_list[low:high//2])
    """if target is higher than mid, then recursively calls with same target, same low, new high, and new list from mid+1 to high+1"""
    if int_list[high//2] < target:
        return bin_search(target, 0, len(int_list[high//2+1:high+1])-1, int_list[high//2+1:high+1])