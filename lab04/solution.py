def winner(names,scores):
    maxb=0
    k=0
    for i in range(0,len(scores)):
        if maxb<scores[i]: maxb=scores[i]
    for i in range(0,len(names)):
        if (scores[i]==maxb)and(k==0):
            k=1
            return names[i]
    print(maxb)

def ranking(names,scores):
    for i in range(1,len(names)):
        if scores[i-1]>scores[i]:
            (scores[i-1],scores[i])=(scores[i],scores[i-1])
            (names[i-1],names[i])=(names[i],names[i-1])
    return (names)

names=[]
scores=[]
# for i in range (0,3):
#     names.append(input())
#     scores.append(int(input()))
print(winner(names,scores))
sr=sum(scores)/len(scores)
print(round(sr,2))
print(ranking(names,scores))
for i in range (0,len(names)):
    if scores[i]>sr: print(names[i])


