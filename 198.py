def rob(arr, i, dictionary):
    if i==0:
        money = arr[0]
    elif i==1:
        money = max(arr[0:2])
    elif i in dictionary:
        money = dictionary[i]
    else:
        money = max([rob(arr, i-2, dictionary)+arr[i], rob(arr, i-1, dictionary)])
        dictionary[i] = money
    return money
arr = [1,2,3,1]
d1 = {}
print(rob(arr, len(arr)-1, d1))
