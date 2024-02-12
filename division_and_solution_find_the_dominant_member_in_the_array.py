def First(array, n):
    beg = 0
    end = len(array) - 1
    while (beg <= end):
        mid = int(beg + (end-beg)/2)
        if (array[mid] == n):
            if (mid-1 >= 0 and array[mid-1] == n):
                end = mid-1
                continue
            return mid
        elif (array[mid] < n):
            beg = mid + 1
        else:
            end = mid - 1
    return -1
def Last(array, n):
    beg = 0
    end = len(array)-1
    while (beg <= end):
        mid = int(beg + (end-beg)/2)
        if (array[mid] == n):
            if (mid+1 < len(array) and array[mid+1] == n):
                beg = mid + 1
                continue
            return mid
        elif (array[mid] < n):
            beg = mid + 1
        else:
            end = mid - 1
    return -1
def sortlist(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2
        left = unsorted_array[:mid]
        right = unsorted_array[mid:]
        sortlist(left)
        sortlist(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1
array = [1, 1, 1, 9, 9, 9, 1, 9, 9, 9]
print(f"Given array is: {array}")
sortlist(array)
dom_num = len(array)//2
print(f"Dom repeat is : {dom_num}")
for n in list(set(array)):
    first_index = First(array, n)
    last_index = Last(array, n)
    i_repeat = last_index - first_index + 1
    if (i_repeat >= dom_num):
        print(f"the num {n} repeats {i_repeat} times")
