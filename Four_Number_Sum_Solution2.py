# write a function that takes in an array of distinct
# integer and a target number
# this function retrun a list of all quadruplets 
# each of which sum up to the target num
# if no such quadruplet, return an empty list

def fourNumberSum2(array, targetSum):
    # Write your code here.
    qua_dict = {}
    quadruplet = []
	
    get_rtn_list(array, targetSum, qua_dict, quadruplet, 0)
    rtn_list = [x for x in qua_dict.values()]
    return rtn_list

def	get_rtn_list(array, targetSum, qua_dict, quadruplet, start_idx):
    if len(quadruplet) == 4:
        if sum(quadruplet) == targetSum:
            temp_qua = sorted(quadruplet)
            num_to_str = [str(x) for x in temp_qua]
            qua_str = ''.join(num_to_str)
            if qua_str not in qua_dict:
                qua_dict[qua_str] = temp_qua
        return
    for idx in range(start_idx, len(array)):
        # put current value in
        val = array[idx]
        quadruplet.append(val)
        get_rtn_list(array, targetSum, qua_dict, quadruplet, idx + 1)
		# skip current value
        quadruplet.pop()

array = [7,6,4,-1,1,2]
targetSum  = 16

print(fourNumberSum2(array, targetSum))