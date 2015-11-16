
def mcd(a, b):
    if ( a == b):
        return a
    else:
        if ( a > b):
            return(mcd(a-b, b))
        else:
            return(mcd(a, b-a))

x = int(input("Give me a number: "))
y = int(input("Give me another number: "))

print(mcd(x,y))
