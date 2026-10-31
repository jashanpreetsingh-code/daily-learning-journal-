num1 = int(input())
num2 = int(input())
opration = input("select opration = +,-,*,/,%,,** ")

if opration == "+":
    result= num1+num2 
    print(result) 

elif opration == "-":
    result= num1-num2
    print(result)

elif opration == "*":
    result=num1*num2
    print(result)

elif opration == "/":
    result=num1/num2
    print(result)

elif opration == "%":
    result= num1 % num2
    print(result)

    
else :
    print("Invalid")