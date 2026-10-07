num = int(input("Enter a number: "))

def check_num(num):
    if num > 0:
        return("Positive number")
    elif num < 0:
        return("Negative number")
    else:
        return("Zero")