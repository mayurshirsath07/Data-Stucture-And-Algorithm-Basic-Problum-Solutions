def threesum(arr,target):
    n=len(arr)

    for i in range(n-2):
        for j in range (i+1, n-1):
            for k in range(j+1, n):
                if arr[i]+arr[j]+arr[k]==target:
                    return True
                    return False
            
if __name__=="__main__":
    arr=[1,4,45,6,10,8]
    target=13
    if threesum(arr,target):
        print('true')
    else:
        print('false')
        

    