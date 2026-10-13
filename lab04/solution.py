def winner(names,scores):
    maxb=-999999999
    k=0
    for i in range(0,len(scores)):
        if maxb<scores[i]: maxb=scores[i]
    for i in range(0,len(names)):
        if (scores[i]==maxb)and(k==0):
            k=1
            return names[i]
    print(maxb)

def ranking(names, scores):
    return [
        name for score, name in sorted(
            zip(scores, names),
            key=lambda x: x[0],
            reverse=True
        )
    ]

def average(scores):
    if len(scores)==0:
        return 0
    return round(sum(scores)/len(scores),2)

def above_average(names, scores):
    sr = average(scores)
    newnames = []
    for i in range(len(names)):
        if scores[i] > sr:
            newnames.append(names[i])
    return newnames

# names=[]
# scores=[]
# for i in range (0,3):
#     names.append(input())
#     scores.append(int(input()))
# print(winner(names,scores))
# print(average(names,scores))
# print(ranking(names,scores))
# print(above_avarage(names,scores,average(names,scores)))



