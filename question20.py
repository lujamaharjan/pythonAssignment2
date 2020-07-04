'''
    Write a python class to find the three elements that 
    sum to zero from a list of n real numbers.

    Input array: [-25, -10, -7, -3, 2, 4, 8, 10]
    Output : [[-10, 2, 8], [-7, -3, 10]]
'''
def sums_zero(arr):
    result = []
    # finding numbers that sum zero
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            for k in range(2, len(arr)):
                if(arr[i] + arr[j] + arr[k] == 0):
                    result.append([arr[i],arr[j], arr[k]])
                    
    # numbers are repeting so makeing numbers non repeting                
    temp = []
    for i in result:
        if sorted(i) not in temp:
            temp.append(sorted(i))
    return temp


print(sums_zero([-25, -10, -7, -3, 2, 4, 8, 10]))




