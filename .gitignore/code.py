tests=int(input())
team = input("Number of teams and number of qualifying teams?")
team_arr=team.split()
pTeam = int(team_arr[0])
qTeam = int(team_arr[1])
assert(pTeam>qTeam),"Qualifying teams must be less than Participating teams"
scores=input("Enter scores of each team").split()
for i in range(len(scores)):
    scores[i]=int(scores[i])

scores.sort(reverse=True)
#print(scores)


ctr=0

minScore=scores[qTeam-1]
for i in range(qTeam,pTeam):
    if(scores[i]==minScore):
        ctr=ctr+1

ans=ctr+qTeam
       
print(ans)
