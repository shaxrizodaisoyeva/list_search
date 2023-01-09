def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    data1=[]
    a=0
    d=min(data)
    while a<len(data):
        if data[a]%2!=0:
            c=data1.append(data[a])
        a+=1
        if data1:
            d=min(data1)
        else:
            d=-1
    return d
data=[23,55,1,4,6,89,199,46,34,87,106,208]
print(find_min_odd(data))
    

