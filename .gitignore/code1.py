n = int(input())
for x in range(0, n):
    numPeople = int(input())
    assert(numPeople >= 2),"Number of people must be more than 1"
    
    A = input()
    AiList = A.split()
    for i in range(0,len(AiList)) :
        AiList[i] = int(AiList[i])
    day = 0
    people = 1
    peoplek=0
    peoplej=0
    j=0
    while(people < numPeople):
        
        peoplek=peoplek+peoplej
        peoplej=0
        for j in range(people-1,people+peoplek):
            if(j < len(AiList)):
                peoplej = peoplej + AiList[j]
        people=people+peoplek+peoplej
        
        
        day = day + 1    
    print(day)
