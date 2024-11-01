def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = [num for bucket in buckets for num in bucket]

    return sorted_arr

