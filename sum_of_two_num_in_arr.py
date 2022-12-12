def twoSum(arr, sum):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[i] + arr[j] == sum):
                print(str(arr[i]) + " " + str(arr[j]))
                return i, j

arr = [1, 3, 5, 6, 11, 23]
sum = 9
print("Indices: "+str(twoSum(arr, sum)))
