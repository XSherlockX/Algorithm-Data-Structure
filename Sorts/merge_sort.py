def merge_sort(arr):
    if len(arr) > 1:
        mid  = int(len(arr) /2)
        leftArr = arr[:mid]
        rightArr = arr[mid:]
        merge_sort(leftArr)
        merge_sort(rightArr)
        merge(arr, leftArr, rightArr)

def merge(arr, leftArr, rightArr):
    i = j = k = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i = i +1
        else:
            arr[k] = rightArr[j]
            j = j +1
        k = k +1
    while i < len(leftArr):
        arr[k] = leftArr[i]
        k = k +1
        i = i +1
    while j < len(rightArr):
        arr[k] = rightArr[j]
        k = k +1
        j = j +1
      
