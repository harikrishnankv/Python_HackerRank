def fizz_buzz(number):
    if num%3==0:
        if num%5==0:
            return "fizzbuzz"
        else:
            return"fizz"
    elif num%5==0:
        return "buzz"
    else:
        return number



num=int(input('enter a number '))
print(fizz_buzz(num))