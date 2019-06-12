def search():
    value=input()
    return value
def inputt():
    count = int(input())
    inputs=[]
    for i in range (0,count):
        inputs.append(list(input().split()))
    l1=len(inputs)
    p = search()
    for i in range (0,l1):
        s=inputs[i]
        if s[0]==p:
            s.pop(0)
            length=len(s)
            s=[int(x) for x in s]
            sum=0
            for i in s:
                sum+=i
            sum=(sum/length)

    return sum
def main():
    print("{0:.2f}".format(inputt()))

main()
