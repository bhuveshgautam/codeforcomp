t=int(input())
for i in range(t):
    dic={}
    n=int(input())
    time=0
    for j in range(n):
        word=input()
        if word not in dic :
            tword=0
            for k in range(len(word)):
                if(k==0):
                    tword=tword+0.2
                else:
                    if((word[k]=='d' or word[k]=='f') and (word[k-1]=='d' or word[k-1]=='f')):
                        tword=tword+0.4
                    elif((word[k]=='d' or word[k]=='f') and (word[k-1]=='j' or word[k-1]=='k')):
                        tword=tword+0.2
                    elif((word[k]=='j' or word[k]=='k') and (word[k-1]=='j' or word[k-1]=='k')):
                        tword=tword+0.4
                    elif((word[k]=='j' or word[k]=='k') and (word[k-1]=='d' or word[k-1]=='f')):
                        tword=tword+0.2
            time=time+tword
            dic[word]=tword
        else:
            time=time+(dic[word])/2
    print(round(time*10))
