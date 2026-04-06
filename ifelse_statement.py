if year % 4 == 0:
    days = 366
else:
    days = 365

#Assume the variable s has been assigned a string. Write code that displays "stop" if s is equal to "end". Otherwise, display "go".#
    if s == "end":
    print("stop")
else:
    print("go")
#Assignment: Assume that a and b have been assigned two different float values. Write a (possibly nested) if-elif-else statement that compares b - a and makes the following assignments, based on the result:#
if b - a < 0:
    low = 1
    high = 0
elif b - a > 0:
    low = 0
    high = 1
else:
    low = 0
    high = 0
