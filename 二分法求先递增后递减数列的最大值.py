def find_max(lst):
    if not lst or not isinstance(lst, list):
        print('lst is empty or type is not list')
        return None

    for index, item in enumerate(lst):
        if item > lst[index + 1]:
            return item


lst = [1, 3, 6, 8, 5, 3, 2]
max_value = find_max(lst)
print(max_value)


def find_max_num(arr):
    length = len(arr)
    if length == 0:
        return -1
    left = 0
    right = length - 1
    mid = left + (right - left) // 2
    while mid > 0 and mid < length - 1:
        if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
            return arr[mid]
        elif arr[mid] > arr[mid - 1]:
            left = mid + 1
            mid = left + (right - left) // 2
        else:
            right = mid - 1
            mid = left + (right - left) // 2
    return -1


print(find_max_num([0, 1, 4, 7, 9, 0, -1]))
