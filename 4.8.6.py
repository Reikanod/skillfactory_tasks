def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i, j, result = 0, 0, []
    # переварачиваем оба массива и из конца будем удалять элемент, который добавляем в результирующий массив
    left.reverse()
    right.reverse()
    # пока не кончится одна из половинок массива
    while left and right:
        if left[-1] >= right[-1]: # сравниваем и наименьший элемент в результирующий массив, удаляя его из половинки
            result.append(right.pop())
        else:
            result.append(left.pop())

    if left: # в том массиве, в котором остался хвост сохраняем в новый список
       tail = left
    else:
        tail = right

    while tail: # хвост добавляем в результирующий массив в конец
        result.append(tail.pop())

    return result

arr = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(merge_sort(arr))

