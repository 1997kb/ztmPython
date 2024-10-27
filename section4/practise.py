arr = [1,2,4,4]

target = 8

l,r = 0,len(arr)-1
while l  < r:
    if arr[l] + arr[r] < target:
        l+=1
    elif arr[l] + arr[r] > target:
        r-=1
    else:
        print(l,r)
        break
    

