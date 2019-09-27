def max_list_iter(int_list):
	pass  
	if int_list == []:
		return None
	if int_list == None:
		raise ValueError('List is None')
	else:
		max_int = int_list[0]
		for i in range(len(int_list)):
			if int_list[i] > max_int:
				max_int = int_list[i]
		return max_int

def reverse_rec(int_list):
	pass
	rev_list = []
	if int_list == None:
		raise ValueError("list is None")
		
	if int_list == []:
		return []
	#return int_list[0] + reverse_rec(int_list[1:])
	return int_list[len(int_list) - 1] + reverse_rec(int_list[0,len(int_list)-1])

def bin_search(target, low, high, int_list): 
	if int_list == None:
   	    raise ValueError("List is None")
   	if len(int_list) == 0:
   		return None
   	if int_list[high//2] == target:
   		return target
   	if int_list[high//2] > target:
   		return bin_search(target, low, high//2, int_list[low:high//2])
   	if int_list[high//2] < target:
   		return bin_search(target, high//2, high, int_list[high//2+1:high+1])

