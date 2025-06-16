def max_array(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num 
    return max_num

arr = [5, 3, 8, 2, 9, 1]
print("Maximum NUmber: ",max_array(arr))