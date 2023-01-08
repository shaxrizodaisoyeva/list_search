def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    a=len(data)
    b=data.index(data[(a-1)])
    return b
data=[1,2,3,4,5,6,7,8,9,10,11,19,13]
print(find_max_index(data))
