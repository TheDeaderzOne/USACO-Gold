input = open("cardgame.in","r")
output = open("cardgame.out","w")
CardNum = int(input.readline().replace("\n",""))
BessieList = []; FirstElsieList = []; SecondElsieList = []

for x in range(int(2*CardNum)):
    BessieList.append(x+1)

for _ in range(CardNum):
    hu = int(input.readline().replace("\n",""))
    if _ < int(CardNum/2):
        FirstElsieList.append(hu)
    else:
        SecondElsieList.append(hu)
    BessieList[hu-1]=0

FirstElsieList.sort()
SecondElsieList.sort()
BessieList.sort()

while BessieList[0]==0:
    BessieList.pop(0)

def HighCardGreedy(BesList,ElsList):
    wins = 0
    pointer = len(ElsList)-1
    while pointer != -1:
        if BesList[-1]>ElsList[pointer]:
            wins+=1
            BesList.pop(-1)
            pointer-=1
        else:
            pointer-=1
    return wins

def LowCardGreedy(BeList,ElList):
    vins = 0
    pointer = 0
    while pointer != len(ElList):
        if BeList[0]<ElList[pointer]:
            vins+=1
            BeList.pop(0)
            pointer+=1
        else:
            pointer+=1
    return vins

FirstHalf = HighCardGreedy(BessieList,FirstElsieList)
SecondHalf = LowCardGreedy(BessieList,SecondElsieList)

output.writelines(str(FirstHalf+SecondHalf))