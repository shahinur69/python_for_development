res = 0.0
try:
   number = int(input("enter a number: "))
   div = int(input("enter a divisor: "))
   res = number/div
except ZeroDivisionError as z:
    res = number/1
    print(res)
except ValueError as v:
    res = number/2
    print(res)
finally:
    print(res)
