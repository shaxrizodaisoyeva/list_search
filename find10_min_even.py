def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    data1=[]
    a=0
    d=min(data)
    while a<len(data):
        if data[a]%2==0:
            b=data1.append(data[a])
        a+=1
        if data1:
            d=min(data1)
        else:
            d=-1
    return d
data=[1,56,78,34,4,6,89,46,34,88,106,199,34,89]
print(find_min_even(data))
    

