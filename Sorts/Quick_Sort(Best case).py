#-------------Sort-----------------------


def Sort(arr, s, e):
    pivot = arr[s]
    i = s + 1
    j = e

    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break

    arr[s], arr[j] = arr[j], arr[s]
    return j

#---------------Quick Sort-------------------

def quick_sort(arr, s, e):
    if s < e:
        m = Sort(arr, s, e)
        quick_sort(arr, s, m - 1)
        quick_sort(arr, m + 1, e)



#------------------Inputs--------------------
arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr) - 1)


#-------------------Print---------------------
print(" ".join(map(str, arr)))
