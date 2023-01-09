def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    data1=[]
    a=0
    d=max(data)
    while a<len(data):
        if data[a]%2==0:
            b=data1.append(data[a])
        a+=1
        if data1:
            d=max(data1)
        else:
            d=-1
    return d
data=[1,4,6,89,46,34,88,106,199,34,89]
print(find_max_even(data))
