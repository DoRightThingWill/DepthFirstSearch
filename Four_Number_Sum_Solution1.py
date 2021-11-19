# write a function that takes in an array of distinct
# integer and a target number
# this function retrun a list of all quadruplets 
# each of which sum up to the target num
# if no such quadruplet, return an empty list

def fourNumberSum(array, targetSum):
    # Write your code here.
	# array = [7,6,4,-1,1,2]
	qua_dict = {}
	quadruplet = []
	
	get_quadruplet(array, targetSum, quadruplet, 0, qua_dict)
	rtn_list = [x for x in qua_dict.values()]
	return rtn_list
def	get_quadruplet(array, targetSum, quadruplet, arr_idx, qua_dict):
	# print("************")
	# print("quadruplet len", len(quadruplet))
	# print("arr_idx", arr_idx)
	# if arr_idx >= len(array):
	# 	return
	
	if len(quadruplet) == 4:
		if sum(quadruplet) == targetSum:
			sorted_quadruplet = sorted(quadruplet)
			str_list =[str(x) for x in sorted_quadruplet]
			str_num = ''.join(str_list)
			if str_num not in qua_dict:
				qua_dict[str_num] = sorted_quadruplet
		return 

	
	for idx in range(arr_idx, len(array)):
		val = array[idx]

		if len(quadruplet) < 4:
			quadruplet.append(val)
		get_quadruplet(array, targetSum, quadruplet, idx + 1, qua_dict)
		# do not take this value
		if len(quadruplet) > 0:
			quadruplet.pop()

    
array = [7,6,4,-1,1,2]
targetSum = 16

print(fourNumberSum(array, targetSum))