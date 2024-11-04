#-----------------Sort-------------------

def Sort(arr, s, e):
    pivot = arr[s]
    i = s + 1
    j = e

    while 1:
        while i <= j and arr[i] < pivot: #peyda kardan i
            i += 1
        while i <= j and arr[j] > pivot:#peyda kardan j
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] #jabejayye i, j
            i += 1
            j -= 1
        else:
            break


    # avaz kardan jaye pivot ba j

    temp = arr[s]
    arr[s] = arr[j]
    arr[j] = temp  

    return j


#---------------Quick Sort-------------------


def quickselect(arr, s, e, k):
    if s <= e:
        a = Sort(arr, s, e) # gereftan meghdar j

        if a == k:
            return arr[a]
        elif a > k:
            return quickselect(arr, s, a - 1, k)
        else:
            return quickselect(arr, a + 1, e, k)

    return -1  # vorodi eshtebah bashe


#------------------------Input-----------------------
arr = list(map(int, input().split()))
k = int(input()) - 1  # tabdil andis


result = quickselect(arr, 0, len(arr) - 1, k)


print(result)
