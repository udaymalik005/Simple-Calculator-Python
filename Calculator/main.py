try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second   number: "))

    print("What kind of Operation Do you want to perform.\nPress + for Addition\nPress - for Substraction\nPress * for Multiflication\nPress / for Division")

    O = input("Enter Operation: ")
    match O:
        case"+":
            print(f"The Result is: {a+b}")
        case"-":
            print(f"The Result is: {a-b}")
        case"*":
            print(f"The Result is: {a*b}")
        case"/":
            print(f"The Result is: {a/b}")
        case default:
            print(f"There is an Error")



except Exceptionas as e:
    print("Enter a valid value of a and b")
