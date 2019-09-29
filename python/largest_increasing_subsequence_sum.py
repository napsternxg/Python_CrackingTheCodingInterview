def largest_increasing_subsequence_sum(arr):
    """Identify the largest increasing subsequence sum for a given array."""
    liss_values = []
    for i, v in enumerate(arr):
        i_sum = arr[i]
        i_idx = i
        print(i, liss_values)
        for j in range(i):
            if arr[j] < arr[i]:
                if arr[i] + liss_values[j] > i_sum:
                    i_idx = j
                    i_sum = arr[i] + liss_values[j]
        print("i={}, i_idx={}, i_sum={}".format(i, i_idx, i_sum))
        liss_values.append(i_sum)
    liss = max(liss_values)
    return liss
    
    
    
    
if __name__ == "__main__":
    import sys
    arr = [int(v) for v in sys.argv[1:]]
    print(arr)
    if len(arr) == 0:
        arr = [5, 15, -30, 10, -5, 40, 10]
    liss = largest_increasing_subsequence_sum(arr)
    print("largest_increasing_subsequence_sum({}) = {}".format(arr, liss))