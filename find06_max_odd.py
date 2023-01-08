def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    a=0
    while a<len(data):
        if data[a]%2!=0:
            b=data[a]
        a+=1
    return b
data=[1,4,6,89,46,34,88,106,199]
print(find_max_odd(data))