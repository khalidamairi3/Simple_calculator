from addition import add
from  subtraction import subtract
from multiplication import multiply
from division import divide


print("welcome to simple calculator")

print("1) add 2 numbers")
print("2) subtract 2 numbers")
print("3) mutiply 2 numbers")
print("4) divide 2 numbers")

option = input("choose the calculation option: " )

while(int (option) not in [1,2,3,4]):

    print("please enter a number between 1 and 4")
    print("1) add 2 numbers")
    print("2) subtract 2 numbers")
    print("3) mutiply 2 numbers")
    print("4) divide 2 numbers")    
    option = input("choose the calculation option: " )


a= input("enter your first number: ")

while (1):
    try:
        a=float(a)
        break
    except:
        print("only numbers allowed")
        a= input("enter your first number: ")

b=input("enter you second number: ")

while (1):
    try:
        b=float(b)
        break
    except:
        print("only numbers allowed")
        b= input("enter your second number: ")




calculate = {
    "1" : add(a,b),
    "2" : subtract(a,b),
    "3" : multiply(a,b),
    "4" : divide(a,b)
}

print(calculate.get(option))