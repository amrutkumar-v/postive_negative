def check_num(num):
    if num > 0:
        return("Positive number")
    elif num < 0:
        return("Negative number")
    else:
        return("Zero")
print("The result is:",check_num(10))
print("The result is:",check_num(-10))
print("The result is:",check_num(0))