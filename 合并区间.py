def merge(intervals):
    intervals.sort(key=lambda x: x[0])  # 按照intervals的起始索引 从小到大排序
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:  # 理论依据 所有能够合并的区间都必然是连续的
            # interval[0] <= merged[-1][1]，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
