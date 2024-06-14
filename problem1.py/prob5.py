age=int(input("enter your age: "))
if age<18: 
    print("you are not allowed for voting,\nyou will be able to participate after",18-age,"year")
else:
    print("you are allowed to participate voting.")