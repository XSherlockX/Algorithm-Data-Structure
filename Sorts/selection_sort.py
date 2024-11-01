def SelectionSort(arr): 

    length = len(arr)

    for step in range(length):
        min = step
        for j in range(step + 1,length):
            if arr[j] < arr[min]:
                min = j

        arr[step], arr[min] = arr[min] , arr[step]
