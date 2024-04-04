class Figure:
    def __init__(self, figType, point):
        self.figType = figType
        self.point = point

    def check_move(self, new_point) -> bool:
        if(self.point == new_point):
            print("error! Same point to move")
            return False
        elif(int(new_point[1]) < 1 or int(new_point[1]) > 8 or ord(new_point[0]) < 65 or ord(new_point[0]) > 72):
            print("error! Point should be from A1 to H8")
            return False
        else:
            return True
        
    def _move(self, new_point):
        self.point = new_point

class King(Figure):
    def __init__(self, point):
        super().__init__("King", point)

    def move(self, new_point):
        if(Figure.check_move(self, new_point) == 1):
            if(self.point[0] == new_point[0]): 
                if(abs(int(self.point[1]) - int(new_point[1])) == 1):
                    self._move(new_point)
                else:
                    print("error! Invalid move for King")
            elif(abs(ord(self.point[0]) - ord(new_point[0])) == 1):
                self._move(new_point)
            else:
                pass
        else:
            pass


class Rook(Figure):
    def __init__(self, point):
        super().__init__("Rook", point)

    def move(self, new_point):
        if(Figure.check_move(self, new_point) == 1):
            if(self.point[0] == new_point[0] or self.point[1] == new_point[1]): 
                self._move(new_point)              
            else:
                print("error! Invalid move for Rook")
        else:
            pass


class Knight(Figure):
    def __init__(self, point):
        super().__init__("Knight", point)

    def move(self, new_point):
        if(Figure.check_move(self, new_point) == 1):
            if(abs(ord(self.point[0]) - ord(new_point[0])) == 1): 
                if (abs(int(self.point[1]) - int(new_point[1])) == 2):
                    self._move(new_point)
                else:
                    print("error! Invalid move for Knight")              
            elif(abs(ord(self.point[0]) - ord(new_point[0])) == 2):
                if (abs(int(self.point[1]) - int(new_point[1])) == 1):
                    self._move(new_point) 
                else:
                    print("error! Invalid move for Knight")
            else:
                print("error! Invalid move for Knight")
        else:
            pass

