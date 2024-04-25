
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    case 10: 
        print("matched")
    case 20:
        print("matched")
    case _ if x!=30:
        print(x,"is not 50")
    case _ if x!=60:
        print(x,"is not 50")
    case _ :
        print(x)