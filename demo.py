def max_min(arr):
    i = 1
    max = 0
    
    while i < len(arr):
        if arr[i] > arr[max]:
            max = i
        
        i += 1
    
    return arr[max]
