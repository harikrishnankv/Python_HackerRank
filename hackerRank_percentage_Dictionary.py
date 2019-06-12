
def GetStudentRecord(studentRecords, name):
    return studentRecords[name]

def CalculateAverage(studentRecord):
    sum=0
    for mark in studentRecord:
        sum+=mark
    return sum/len(studentRecord)

def MakeStudentRecords():
    numStudents = int(input("Enter the number of students: "))

    studentRecords={}
    s=[]
    for i in range (0,numStudents):
        s=input("Enter student name and marks: ").split()
        studentName=s.pop(0)
        s=[float(x) for x in s]
        studentRecords[studentName]=s
    return studentRecords

def main():

    studentRecords=MakeStudentRecords()
    studentRecord=GetStudentRecord(studentRecords, input("Enter the name of the student:"))
    print("{0:.2f}".format(CalculateAverage(studentRecord)))

main()

'''
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
'''
