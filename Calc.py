def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

if __name__ == "__main__":
    num1 = float(input("Enter 1st"))
    num2 = float(input("Enter 2nd"))

    result = add(num1, num2)
    print(result)
    result = sub(num1, num2)
    print(result)
    result = mul(num1, num2)
    print(result)
    result = div(num1, num2)
    print(result)

