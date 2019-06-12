#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.

    l=len(s)-1

    if s[(l-1):]=="AM":
        s=s.replace("AM","")
        listt=[str(x) for x in s.split(":")]
        if int(listt[0])==12:
            listt[0]="00"
        else:
            pass
        return(f"{listt[0]}:{listt[1]}:{listt[2]}")


    elif s[(l-1):]=="PM":
        s=s.replace("PM","")
        listt=[str(x) for x in s.split(":")]
        if int(listt[0])==12:
            return (f"{listt[0]}:{listt[1]}:{listt[2]}")
        else:
            listt[0]=int(listt[0])+12
            return(f"{listt[0]}:{listt[1]}:{listt[2]}")


s =str(input())

result = timeConversion(s)
print(result)

