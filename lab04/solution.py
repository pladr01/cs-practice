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
    newnames=names[:]
    newnames=sorted(zip(scores,newnames),reverse=True)
    newnames=[newnames[i][1] for i in range(0,len(newnames))]
    return (newnames)

def average(names,scores):
    return round(sum(scores)/len(scores),2)

def above_avarage(names,scores,sr):
    newnemes=[]
    for i in range(0,len(names)):
        if scores[i]>sr:newnemes.append(names[i])
    return newnemes

names=[]
scores=[]
for i in range (0,3):
    names.append(input())
    scores.append(int(input()))
print(winner(names,scores))
print(average(names,scores))
print(ranking(names,scores))
print(above_avarage(names,scores,average(names,scores)))



