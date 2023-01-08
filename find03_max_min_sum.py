def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    a=max(data)
    b=min(data)
    c=int(a)+int(b)
    return c 
data=[1,5,8,3,9,23]
print(find_max_min_sum(data))
