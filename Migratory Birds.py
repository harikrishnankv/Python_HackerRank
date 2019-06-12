getListSize=int(input("enter size of list: "))
spottedBirds=input("enter bird list ").split()
spottedBirds=[int(x) for x in spottedBirds]
tempList=[]
newList=spottedBirds.copy()
newList.sort()
print(newList)
lengthOfNewList=len(newList)
listElement=newList[0]
firstIndex=0
lastIndex=0
for i in range(0,lengthOfNewList):
    if listElement!=newList[i]:
        tempList.append(newList[firstIndex:i])
        firstIndex=i
        listElement=newList[i]
        lastIndex=i
    if i==(lengthOfNewList-1):
        if len(newList[lastIndex:lengthOfNewList])>0:
            tempList.append(newList[lastIndex:lengthOfNewList])
        else:
            tempList.append(newList[i])
tempvalue=0
for birdList in tempList:
    if tempvalue<len(birdList):
        tempvalue=len(birdList)
        maxBirdSet=birdList
print(tempList)
print(maxBirdSet[0])


# 1 2 2 3 4 5 5 1 1 1


