import math
def  euler(digits):
    suma = 0
    for i in range(0, digits+1):
        num = float(math.factorial(i))
        suma += float(1/num)
    return round(suma, digits)

num = int(input("Write the number of decimal points: "))
print("The value of e is: ", euler(num))
