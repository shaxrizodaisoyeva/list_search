def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    data1=[]
    a=0
    while a<len(data):
        if data[a]%2!=0:
            c=data1.append(data[a])
        a+=1
        if data1:
            d=max(data1)
    return d
data=[1,4,6,89,199,46,34,87,106]
print(find_max_odd(data))
