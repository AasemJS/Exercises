def sum_array(num_list):
    if len(num_list) == 0:
        return 0
    return num_list[0] + sum_array(num_list[1:])