
tryAgain = True
while tryAgain == True:
    print("\n[A] Addition")
    print("[B] Subtraction")
    print("[C] Multiplication")
    print("[D] Division")

    choice = input("\nChoice?: ").upper()

    if choice == "A":
        print("\nADDITION")
        num1 = int(input("1st: "))
        num2 = int(input("2nd: "))
        sum = num1 + num2
        print("Sum: ", sum)

        again = input("\nTry Again? [Y/N]: ").upper()
        if again == "Y":
            tryAgain = True

        else:
            print("Thank you")
            tryAgain = False

    elif choice == "B":
        print("\nSUBTRACTION")
        num1 = int(input("1st: "))
        num2 = int(input("2nd: "))
        diff = num1 - num2
        print("Difference: ", diff)

        again = input("\nTry Again? [Y/N]: ").upper()
        if again == "Y":
            tryAgain = True

        else:
            print("Thank you")
            tryAgain = False

    elif choice == "C":
        print("\nMULTIPLICATION")
        num1 = int(input("1st: "))
        num2 = int(input("2nd: "))
        prod = num1 * num2
        print("Product: ", prod)

        again = input("\nTry Again? [Y/N]: ").upper()
        if again == "Y":
            tryAgain = True

        else:
            print("Thank you")
            tryAgain = False

    elif choice == "D":
        print("\nDIVISION")
        num1 = int(input("1st: "))
        num2 = int(input("2nd: "))
        q = num1 / num2
        print("Quotient: ", q)

        again = input("\nTry Again? [Y/N]: ").upper()
        if again == "Y":
            tryAgain = True

        else:
            print("Thank you")
            tryAgain = False

    else:
        print("INVALID INPUT!!!")
        tryAgain = True
