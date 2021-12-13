#Yifeng Xiong
#14648645
#class Faller
#This is a basic class of the game. It defines the attributes of fallers in the game.
#Fallers contains three jewels, each of the jewel has color, row number, col number.
#Three jewels have the same col number.
#Fallers can move to right, left, or descend.
#Fallers can rotate.

class Faller:

    def __init__(self, col: int, color_1: str, color_2: str, color_3: str):
        self._jewel_top_row = None
        self._jewel_top_col = None
        self._jewel_top_color = color_1
        
        self._jewel_middle_row = None
        self._jewel_middle_col = None
        self._jewel_middle_color = color_2
        
        self._jewel_bottom_row = 0
        self._jewel_bottom_col = col
        self._jewel_bottom_color = color_3

    def col(self) -> int:
        return self._jewel_bottom_col

    def top_row(self) -> int or None:
        return self._jewel_top_row

    def middle_row(self) -> int or None:
        return self._jewel_middle_row

    def bottom_row(self) -> int:
        return self._jewel_bottom_row

    def top_color(self) -> str:
        return self._jewel_top_color

    def middle_color(self) -> str:
        return self._jewel_middle_color

    def bottom_color(self) -> str:
        return self._jewel_bottom_color

    def right(self):
        '''
        move the faller to the right
        change position
        don't change color
        '''
        if self._jewel_top_col != None:
            self._jewel_top_col += 1
            
        if self._jewel_middle_col != None:
            self._jewel_middle_col += 1
            
        self._jewel_bottom_col += 1
        
    def left(self):
        '''
        move the faller to the left
        change position
        don't change color
        '''
        if self._jewel_top_col != None:
            self._jewel_top_col -= 1
            
        if self._jewel_middle_col != None:
            self._jewel_middle_col -= 1
            
        self._jewel_bottom_col -= 1

    def descend(self):
        '''
        descend the faller
        change position
        don't change color
        '''
        self._jewel_bottom_row += 1

        if self._jewel_middle_row == None:
            self._jewel_middle_row = 0
        else:
            self._jewel_middle_row += 1

        if self._jewel_middle_row == 1:
            self._jewel_top_row = 0
        elif self._jewel_middle_row > 1:
            self._jewel_top_row += 1

    def rotate(self):
        '''
        rotate the faller
        top -> middle
        middle -> bottom
        bottom -> top
        don't change color
        '''
        self._jewel_top_color, self._jewel_bottom_color = self._jewel_bottom_color, self._jewel_top_color
        
        self._jewel_middle_color, self._jewel_bottom_color = self._jewel_bottom_color, self._jewel_middle_color
    

        
