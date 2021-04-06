def reversePairs(nums):
    cnt = 0
    mergesort(nums, 0, len(nums) - 1, cnt)
    print('this is cnt:', cnt)
    return cnt


def mergesort(nums, l, r, cnt):
    if l < r:
        mid = (l + r) // 2
        mergesort(nums, l, mid, cnt)
        mergesort(nums, mid + 1, r, cnt)
        merge(nums, l, mid, r, cnt)


def merge(nums, l, mid, r, cnt):
    i, j = l, mid + 1
    tmp = []
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    print('this is tmp1:', tmp)
    # 借助归并排序  本题的特殊计算
    ii, jj = l, mid + 1
    while ii <= mid and jj <= r:
        if nums[ii] <= 2 * nums[jj]:
            ii += 1
        else:
            cnt += (mid - ii + 1)
            jj += 1
    if i <= mid:
        tmp += nums[i:mid + 1]
    if j <= r:
        tmp += nums[j:r + 1]
    print('this is tmp2:', tmp)
    for i in range(len(tmp)):
        nums[l + i] = tmp[i]


print(reversePairs([1, 3, 2, 3, 1]))
