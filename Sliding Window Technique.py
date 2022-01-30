

def maxSum(arr, windowSize):
    arraySize = len(arr)
    # n must be greater than k
    if arraySize <= windowSize:
        print("Invalid operation")
        return -1

    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum

    for i in range(arraySize-windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]
        max_sum = max(window_sum, max_sum)

    return max_sum

    


arr = [80, -50, 90, 100]
k = 2
answer = maxSum(arr, k)
print(answer)