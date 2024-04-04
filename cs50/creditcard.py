def checkCard(card) -> bool:
    sum = 0
    intcard = int(card)
    print(intcard)
    for i in range(len(card)):
        if (i%2==0):
            sum = sum + intcard % 10
        else:
            sum = sum + (((intcard % 10) * 2) % 10) + (((intcard % 10) * 2) // 10)
        intcard = intcard // 10
    if(sum % 10 == 0):
        return True
    else:
        return False


    

def enterCard():
    card = input("Enter card\n")
    check = checkCard(card)
    print(f"Card is {check}")


def main():
    enterCard()


if __name__ == "__main__":
    main()    