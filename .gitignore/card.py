test = int(input())
for n in range(test):
    ctr = 0
    N = int(input())
    cards = input().split()
    
    for x in range(N):
        cards[x] = int(cards[x])
    
    i = 1   
    while(i < N and ctr < 2):
        if(cards[i] < cards[i - 1]):
            ctr = ctr + 1
        i = i + 1
            
    if(ctr == 0):
        print('YES')
    elif(ctr == 1):
        if(cards[0] >= cards[N - 1]):
            print('YES')
        else:
            print('NO')
    else:        
        print('NO')
