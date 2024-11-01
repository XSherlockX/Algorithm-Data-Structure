def counting_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    range_of_elements = max_num - min_num + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[arr[i] - min_num] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_num] - 1] = arr[i]
        count_arr[arr[i] - min_num] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]


