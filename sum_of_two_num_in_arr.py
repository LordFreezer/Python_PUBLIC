def twoSum1(arr, sum):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[i] + arr[j] == sum):
#                print(str(arr[i]) + " " + str(arr[j]))
                return arr[i], arr[j]
                
def twoSum2(arr, sum):
    dict = {}
    for i in range(len(arr)):
        dict[sum - arr[i]] = arr[i]
        try:
            return arr[i], dict[arr[i]]
        except KeyError:
            dict[sum - arr[i]] = arr[i]

arr = [1, 3, 5, 6, 11, 23]
sum = 9
print(twoSum2(arr, sum))
