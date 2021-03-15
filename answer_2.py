def findIndex(arr):

    leftSum = 0
    rightSum = 0
    l = 0
    r = len(arr)-1

    while (l < r):
       # print(leftSum,rightSum)
        if (l < r ):
            leftSum += arr[l]
            rightSum += arr[r]

            while (leftSum < rightSum) and (l<r):
                l += 1
                leftSum += arr[l] 

            while (rightSum < leftSum) and (l < r):
                r -=1
                rightSum += arr[r]

                l += 1
                r -= 1

    return l



if __name__ == '__main__':
    s = input()
    inputList = list(map(int, s.split(",")))

    result = findIndex(inputList)
    print(result)
