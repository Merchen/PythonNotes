def merge(left, right):
    l, r = 0, 0
    seq = []
    print('left', left, 'right', right)
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            seq.append(left[l])
            l += 1
        else:
            seq.append(right[r])
            r += 1
    seq.extend(left[l:])
    seq.extend(right[r:])
    return seq


def merge_sort(array):
    length = len(array)
    if length <= 1:
        return array
    mid = int(length / 2.)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)