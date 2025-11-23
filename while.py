              # simple program taht make add even numbers
while True :
    num1=float(input("enter the number one: "))
    sing=input("enter the operator: ")
    num2=float(input("enter the number two: "))
    if sing == "+" :
        print("the resut is : " , num1+num2 )

    elif sing == "-":
        print("the result is : " , num1-num2 )

    elif sing == "*":
        print("the reult is : " , num1*num2 )

    elif sing == "/":
        print("the result is : " , num1/num2 )
    
    else:
        print("done all!")


                 # simple program taht make grade of the results

grade=int(input("enter you grade: "))

if grade >= 90 and grade <= 100:
    print(" you grade is : A ")
elif grade >=80 and grade <= 89:
    print("you grade is : B") 
elif grade >= 70 and grade <= 79:
    print("you grade is : C")
elif grade >= 60 and grade <= 69:
    print("you grade is : D")
elif grade >= 0 and grade <= 59:
    print("you garde is : F ")
else:
    print("thaRE are not that raseult!")


                        #  simple program that make guess number 

secret = 6

guess=int(input("enter the secret number(1-10): "))

while guess != secret:
    guess=int(input("enter the secret number(1-10): "))

print(f"the secret number is : {secret}")
