n = int(input())
for x in range(0, n):
    numPeople = int(input())
    assert(numPeople >= 2)
    
    A = input()
    AiList = A.split()
    for i in range(0,len(AiList)) :
        AiList[i] = int(AiList[i])
        
    day = 0
    people = 1
    peoplek=0
    peoplej=0
    while(people < numPeople):
        
        peoplek = peoplek + peoplej
        peoplej=0
        if people == 1:
            for j in range(people - 1, people + peoplek):
                if(j < len(AiList)):
                    peoplej = peoplej + AiList[j]
        else:
            for j in range(people - peoplek, people):
                if(j < len(AiList)):
                    peoplej = peoplej + AiList[j]
        people = people + peoplek + peoplej
        
        day = day + 1    
    print(day)
