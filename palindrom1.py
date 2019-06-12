t = 1

def pal(x):
        t=1
        p=int(len(x))
        s = int(p/2)+1
        for i in range(0, int(s)):
           # print(x[i],x[p-1-i])
           if x[i] != x[p - i - 1]:
                t = 0
                break

        if t == 0:
            print('not palindrome')
        else:
            print(' palindrome')


word = input('enter the word : ')
pal(word)


