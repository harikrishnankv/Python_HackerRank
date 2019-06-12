
SaveFile1=open("count5000.txt","w")
SaveFile2=open("count10000.txt","w")
SaveFile3=open("count20000.txt","w")
for i in range (0,5001):
    WriteFile1=str(i)+str(" ")
    SaveFile1.write(WriteFile1)
for i in range (0,10001):
    WriteFile2=str(i)+str(' ')
    SaveFile2.write(WriteFile2)
for i in range (0,20001):
    WriteFile3=str(i)+str(' ')
    SaveFile3.write(WriteFile3)

SaveFile1.close()
SaveFile2.close()
SaveFile3.close()

readFile=open("count5000.txt","r").read()
print(readFile)

readFile=open("count10000.txt","r").read()
print(readFile)

readFile=open("count20000.txt","r").read()
print(readFile)