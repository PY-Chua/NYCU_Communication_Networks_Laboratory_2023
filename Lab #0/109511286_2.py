def min_avg_diff(n, nums):
    min_diff, min_index, prefix_sum, suffix_sum = float('inf'), -1, 0, sum(nums)
    for i, num in enumerate(nums):
        prefix_sum += num
        suffix_sum -= num
        prefix_avg = prefix_sum / (i + 1)
        if n - i - 1 != 0:
            suffix_avg = suffix_sum / (n - i - 1)
        else:
            suffix_avg = 0
        diff = abs(prefix_avg - suffix_avg)
        if diff < min_diff:
            min_diff = diff
            min_index = i
    return min_index

n_nums = int(input())
nlist = []
for i in range(n_nums):
    input_str = input().replace(" ", "")
    n = int(input_str[0])
    nums = list(map(int, input_str[1:]))
    nlist.append(min_avg_diff(n, nums))
print(*nlist, sep="\n")