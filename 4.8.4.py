array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(1, len(array)):
    el = array[i]
    ind = i - 1
    while ind > -1 and el < array[ind]:
        array[ind], array[ind + 1] = array[ind + 1], array[ind]
        ind -= 1

print(array)
