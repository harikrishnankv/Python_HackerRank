

def find(value,arrayy):
    s = int(len(arrayy))
    position = "null"
    for i in range(0,s):
        if arrayy[i]==value:


            return True
    return False


inp=int(input("enter number  "))
test=[int(x) for x in input("enter array ").split()]
result=find(value=inp,arrayy=test)
print(result)