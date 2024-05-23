def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i, j, result = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):

    tail = left if i < len(left) else tail = right
    for _ in range(len(tail)):
        result.append(tail.pop())

    return result

arr = [2, 3, 1, 4, 6, 5, 9, 8, 7]
merge_sort(arr)
print(arr)
