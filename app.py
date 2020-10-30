from addition import add
from  subtraction import subtract
from multiplication import multiply
from division import divide




print("welcome to simple calculator")

print("1) add  numbers")
print("2) subtract numbers")
print("3) mutiply numbers")
print("4) divide numbers")

option =int( input("choose the calculation option: " ))

while(option not in [1,2,3,4]):

    print("please enter a number between 1 and 4")
    print("1) add  numbers")
    print("2) subtract  numbers")
    print("3) mutiply  numbers")
    print("4) divide numbers")    
    option = int(input("choose the calculation option: " ))
if option == 3 or option==4:
    result =1
else:
    result=0

choice = True
iteration=0
while(choice == True):
    a= input("enter your number: ")
    while (1):

        try:
            a=float(a)
            break
        except:
            print("only numbers allowed")
            a= input("enter your  number: ")
    if(option == 1):
        result = add(a,result)
    if(option == 2 and iteration == 0):
        result = subtract(a,result)
    elif (option == 2):
        result = subtract(result,a)
    if(option == 3):
        result = multiply(a,result)
    if(option == 4 and iteration == 0):
        result = divide(a,result)
    elif (option == 4):
        result = divide(result,a)
    iteration = iteration+1
    choice = input("do you want to add one more number to youe operation y/n : ")=="y"
    


print(result)