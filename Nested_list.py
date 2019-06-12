noEntries=int(input("Enter Entries: "))
physicsRecord=[]
markList=[]
finalList=[]
for i in range (0,noEntries):
    studentName=input("Enter Name: ")
    physicsMark=float(input("Enter Mark: "))
    physicsRecord.append([studentName,physicsMark])
    markList.append(physicsMark)
copyRecord=physicsRecord.copy()
minValue=min(markList)
for entry in physicsRecord:
    if entry[1]==minValue:
        copyRecord.remove(entry)
        markList.remove(entry[1])
minValue=min(markList)
for entry in physicsRecord:
    if entry[1]==minValue:
        finalList.append(entry)
finalList.sort()
for values in finalList:
    print(values[0])




'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''