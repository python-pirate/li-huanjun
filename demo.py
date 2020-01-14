def select_sort(arr):
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        max = i

        while j < len(arr):
            if arr[j] > arr[max]:
                max = j
            j += 1

        if max != i:
            arr[max], arr[i] = arr[i], arr[max]

        i += 1
