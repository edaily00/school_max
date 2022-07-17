def list_max(num_list):
    length = len(num_list)
    if length == 1:
        return num_list[0]

    if num_list[0] >= num_list[1]:
        num_list.pop(1)
        return list_max(num_list)
    else:
        temp = num_list[1]
        num_list[1] = num_list[0]
        num_list[0] = temp
        num_list.pop(1)
        return list_max(num_list)



