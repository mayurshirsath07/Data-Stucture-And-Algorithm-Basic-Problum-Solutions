# the native approch is to explore all subset of size three and keep a track of the different 
# between target and the sum of the subset . then returns the sum which is colsest to target.

def closestsum(arr,target):
    n=len(arr)
    minDiff=float('inf') #infinity of nums and converted floating nos to positive nos
    res=0

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                currsum=arr[i]+arr[j]+arr[k]
                currDiff=abs(currsum-target)  #returns the absolute values of the nos
                
                #  if current Diff is less than minDiff then it indicates          

                if currDiff<minDiff:
                    res=minDiff=currDiff
                elif currDiff==minDiff:
                    res=max(res,currsum)
                    return res
                
if __name__=="__main__":
    arr=[-1,2,2,4,]
    target=4

    print(closestsum(arr,target))               
                