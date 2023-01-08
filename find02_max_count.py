def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    a=max(data)
    b=data.count(a)
    return b
data=[1,5,67,34,2,67,54,21,67]
print(find_max_count(data))
