# Calculator 

options = ["Addition","Subtraction","Division" ,"Multiplication"]

a = int(input("Enter first Number:" ))
b = int(input("Enter second Number:" ))

choice = input("Enter Your choice:\n 1.Addition\n 2.Subtract\n 3.Division\n 4.Multiplication\n")

print("your choice",choice)

if (choice==  "Addition" ):
    ans = a+b
    print(f"Addition of your entered numbers is {ans} ")

elif (choice== "Subtract" ):
    ans= a-b
    print(f"Subtraction of your entered numbers is {ans} ")

elif (choice== "Division" ):
    ans= a/b
    print(f"Division of your entered numbers is {ans} ")

elif (choice== "Multiplication"):
    ans= a*b
    print(f"Multiplication of your entered numbers is {ans} ")

else:
    print("Please Enter Valid choice !!")