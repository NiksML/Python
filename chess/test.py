import figure

def test():
    #King
    king = figure.King(input("Enter first position of king\n"))
    print(f"King at {king.point}")
    king.move(input("Enter next position of king\n"))
    print(f"King at {king.point}")
    king.move(input("Enter next position of king\n"))
    print(f"King at {king.point}")

    #Rook
    rook = figure.Rook(input("Enter first position of king\n"))
    print(f"Rook at {rook.point}")
    rook.move(input("Enter next position of king\n"))
    print(f"Rook at {rook.point}")

    #Knight
    knight = figure.Knight(input("Enter first position of king\n"))
    print(f"Knight at {knight.point}")
    knight.move(input("Enter next position of king\n"))
    print(f"Knight at {knight.point}")

