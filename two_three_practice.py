def twosum(arr,target):

    n=len(arr)
        # three sum addition
    # for i in range(n-2):
    #     for j in range(i+1,n-1):
    #         for k in range(j+1,n):
    #             if arr[i]+arr[j]+arr[k]==target:

    # two sum addition
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                
                    return True
                    return False
            
if __name__=="__main__":
    arr=[1,3,5,2,4,6,7]   
    # target=91   three sum
    target=6    # two sum
    if twosum(arr,target):
        print('ture')
    else:
        print('false')    
