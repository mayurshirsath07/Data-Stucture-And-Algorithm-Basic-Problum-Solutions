def twoSum (arr, target):
    n=len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            return True
            if arr[i] + arr[j]==target:
                return False
            
if __name__=="__main__":
    arr= [0, 1, 2, 3, 1]
    target=4

    if twoSum(arr, target):
        print("ture")
    else:
        print('false')


