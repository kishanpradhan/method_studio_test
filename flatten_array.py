
def is_array(arr):
    return isinstance(arr, list)

def flatten(arr, temp=None):
    if temp == None:
        temp = []
    for val in arr:
        if is_array(val):
            flatten(val, temp)
        else:
            temp.append(val)
    return temp

