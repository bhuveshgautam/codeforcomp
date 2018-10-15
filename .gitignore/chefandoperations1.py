t=int(input())
for i in range(t):
    arrlen=int(input())
    arr1=input().split()
    arr2=input().split()
    
    for i in range(arrlen):
        arr1[i]=int(arr1[i])
        arr2[i]=int(arr2[i])
        
    for i in range(arrlen-2):
        if(arr1[i]<arr2[i]):
            
            arr1[i+1]=2*(arr2[i]-arr1[i])
            arr1[i+2]=3*(arr2[i]-arr1[i])
            arr1[i]=arr2[i]
            
        elif(arr1[i]>arr2[i]):
            print("NIE")
            break
        
    if(arr1==arr2):
        print("TAK")
