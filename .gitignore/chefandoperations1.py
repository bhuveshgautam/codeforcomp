t=int(input())
for i in range(t):
    arrlen=int(input())
    arr1=input().split()
    arr2=input().split()
    
    for i in range(arrlen):
        arr2[i]=int(arr2[i])
    ctr=0
    for i in range(arrlen):
        for j in range(i,arrlen):
            k=1
            arr1[j]=int(arr1[j])+k
            k=k+1
        if(arr1==arr2):
            ctr=1
            break
        
    if(ctr==1):
        print("TAK")
    if(ctr==0):
        print("NIE")
