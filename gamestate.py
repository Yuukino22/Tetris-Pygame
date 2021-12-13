#Yifeng Xiong
#14648645
#class GameState
#Include board of the game, status of the game, col number ,and row number of the game.
#board and game status can be changed.
#We can create new game.
#Create game with contents.
#Add new faller into the game.
#Move faller right or left.
#Descend the faller.
#Find match jewel and eliminate them.
#Jewels will fall if nothing under them.
#An end game function.
#A judge of whether game over.


from faller import Faller
from jewel import Jewel

class GameState:

    def __init__(self, row: int, col: int):
        self._board = []
        self._row_number = row
        self._col_number = col
        self._status = 'freezing'
        self._faller = None

    def row(self) -> int:
        return self._row_number

    def board(self) -> []:
        return self._board

    def col(self) -> int:
        return self._col_number

    def game_status(self) -> str:
        return self._status

    def faller(self) -> Faller:
        return self._faller

    def change_status(self, status: str):
        self._status = status

    def reset_faller(self):
        self._faller = None

    def new_game(self):
        '''
        create new game with no contents
        '''
        for col in range(self._col_number):
            self._board.append([])
            for row in range(self._row_number):
                self._board[-1].append('   ')

    def new_game_with_contents(self, content: list):
        '''
        create new game with contents
        '''
        for index in range(len(content) - 1, -1, -1):
            for num in range(len(content[index])):
                if content[index][num] != ' ':
                    self._board[num][self.row() - len(content) + index] = Jewel('freezing', content[index][num])

    def add_faller(self, faller: Faller):
        '''
        add new faller into the game
        change game status -> falling
        '''
        self._board[faller.col()][0] = Jewel('falling', faller.bottom_color())
        self._faller = faller
        self._status = 'falling'

    def descend(self):
        '''
        faller descends
        change the board of game
        game status -> falling
        '''
        self._faller.descend()
        faller = self._faller
        self._board[faller.col()][faller.bottom_row()] = self._board[faller.col()][faller.bottom_row() - 1]

        if faller.middle_row() == 0:
            self._board[faller.col()][0] = Jewel('falling', faller.middle_color())
        else:
            self._board[faller.col()][faller.middle_row()] = self._board[faller.col()][faller.middle_row() - 1]

        if faller.top_row() == 0:
            self._board[faller.col()][0] = Jewel('falling', faller.top_color())
        elif faller.top_row() == None:
            pass
        else:
            self._board[faller.col()][faller.top_row()] = self._board[faller.col()][faller.top_row() - 1]
            self._board[faller.col()][faller.top_row() - 1] = '   '

        self._status = 'falling'

    def right(self):
        '''
        faller moves to right
        change the board of game
        game status -> falling
        '''
        self._faller.right()
        faller = self._faller
        self._board[faller.col()][faller.bottom_row()] = self._board[faller.col() - 1][faller.bottom_row()]
        self._board[faller.col() - 1][faller.bottom_row()] = '   '

        if faller.middle_row() != None:
            self._board[faller.col()][faller.middle_row()] = self._board[faller.col() - 1][faller.middle_row()]
            self._board[faller.col() - 1][faller.middle_row()] = '   '

        if faller.top_row() != None:
            self._board[faller.col()][faller.top_row()] = self._board[faller.col() - 1][faller.top_row()]
            self._board[faller.col() - 1][faller.top_row()] = '   '

        if self._board[faller.col()][faller.bottom_row() + 1] == '   ':
            self._board[faller.col()][faller.bottom_row()].change_status('falling')
            if faller.middle_row() != None:
                self._board[faller.col()][faller.middle_row()].change_status('falling')
                if faller.top_row() != None:
                    self._board[faller.col()][faller.top_row()].change_status('falling')

        self._status = 'falling'

    def left(self):
        '''
        faller moves to left
        change the board of game
        game status -> falling
        '''
        self._faller.left()
        faller = self._faller
        self._board[faller.col()][faller.bottom_row()] = self._board[faller.col() + 1][faller.bottom_row()]
        self._board[faller.col() + 1][faller.bottom_row()] = '   '

        if faller.middle_row() != None:
            self._board[faller.col()][faller.middle_row()] = self._board[faller.col() + 1][faller.middle_row()]
            self._board[faller.col() + 1][faller.middle_row()] = '   '

        if faller.top_row() != None:
            self._board[faller.col()][faller.top_row()] = self._board[faller.col() + 1][faller.top_row()]
            self._board[faller.col() + 1][faller.top_row()] = '   '

        if self._board[faller.col()][faller.bottom_row() + 1] == '   ':
            self._board[faller.col()][faller.bottom_row()].change_status('falling')
            if faller.middle_row() != None:
                self._board[faller.col()][faller.middle_row()].change_status('falling')
                if faller.top_row() != None:
                    self._board[faller.col()][faller.top_row()].change_status('falling')

        self._status = 'falling'

    def rotate(self):
        '''
        faller rotates
        change the board of game
        game status -> falling
        '''
        if self._faller != None:
            self._faller.rotate()
        faller = self._faller
        if faller.top_row() != None:
            self._board[faller.col()][faller.top_row()], \
            self._board[faller.col()][faller.middle_row()], \
            self._board[faller.col()][faller.bottom_row()] =  self._board[faller.col()][faller.bottom_row()],\
            self._board[faller.col()][faller.top_row()],\
            self._board[faller.col()][faller.middle_row()]
        elif faller.middle_row() != None:
            self._board[faller.col()][faller.bottom_row()] = self._board[faller.col()][faller.middle_row()]
            self._board[faller.col()][faller.middle_row()] = Jewel(self._board[faller.col()][faller.bottom_row()].status(), faller.middle_color())
        else:
            self._board[faller.col()][faller.bottom_row()] = Jewel(self._board[faller.col()][faller.bottom_row()].status(), faller.bottom_color())
        
    def landing(self):
        '''
        faller landing
        change the board of game
        game status -> landing
        '''
        faller = self._faller
        if faller.top_row() != None:
            self._board[faller.col()][faller.top_row()].change_status('landing')
        if faller.middle_row() != None:
            self._board[faller.col()][faller.middle_row()].change_status('landing')
        if faller.bottom_row() != None:
            self._board[faller.col()][faller.bottom_row()].change_status('landing')

        self._status = 'landing'

    def freezing(self):
        '''
        faller freezing
        change the board of game
        game status -> freezing
        '''
        faller = self._faller
        if faller.top_row() != None:
            self._board[faller.col()][faller.top_row()].change_status('freezing')
        if faller.middle_row() != None:
            self._board[faller.col()][faller.middle_row()].change_status('freezing')
        if faller.bottom_row() != None:
            self._board[faller.col()][faller.bottom_row()].change_status('freezing')

        self._status = 'freezing'
 
    def find_match(self):
        '''
        find three or more jewels of the same color
        horizontally, vertically, or diagonally
        '''
        self._find_col_match()
        self._find_row_match()
        self._find_diagonal_match()


    def _find_col_match(self):
        '''
        find three or more jewels of the same color
        vertically
        '''
        for col in self._board:
            for index in range(len(col) - 2, 0, -1):
                if type(col[index + 1]) == Jewel and type(col[index]) == Jewel and type(col[index - 1]) == Jewel:
                    if col[index + 1].color() == col[index].color() == col[index - 1].color():
                        col[index + 1].change_status('match')
                        col[index].change_status('match')
                        col[index - 1].change_status('match')

                        self._status = 'match'

    def _find_row_match(self):
        '''
        find three or more jewels of the same color
        horizontally
        '''
        for index in range(1, self.col() - 1):
            for row in range(self.row()):
                if type(self._board[index - 1][row]) == Jewel and type(self._board[index][row]) == Jewel and type(self._board[index + 1][row]):
                    if self._board[index - 1][row].color() == self._board[index][row].color() == self._board[index + 1][row].color():
                        self._board[index - 1][row].change_status('match')
                        self._board[index][row].change_status('match')
                        self._board[index + 1][row].change_status('match')

                        self._status = 'match'

    def _find_diagonal_match(self):
        '''
        find three or more jewels of the same color
        diagonally
        '''
        for index_col in range(1, self.col() - 1):
            for index_row in range(1, self.row() - 1):
                if type(self._board[index_col - 1][index_row - 1]) == Jewel and type(self._board[index_col][index_row]) == Jewel and type(self._board[index_col + 1][index_row + 1]) == Jewel:
                    if self._board[index_col - 1][index_row - 1].color() == self._board[index_col][index_row].color() == self._board[index_col + 1][index_row + 1].color():
                        self._board[index_col - 1][index_row - 1].change_status('match')
                        self._board[index_col][index_row].change_status('match')
                        self._board[index_col + 1][index_row + 1].change_status('match')

                        self._status = 'match'
            
    
    def eliminate(self):
        '''
        find out jewels in match status
        change them -> '   '
        '''
        for col in self._board:
            for row in range(len(col)):
                if type(col[row]) == Jewel: 
                    if col[row].status() == 'match':
                        col[row] = '   '

    def fall_after_eliminate(self):
        '''
        if there are jewels in faller don't appear on the board but jewels under them have been eliminated
        these jewels should fall
        '''
        faller = self._faller
        if faller.middle_row() == None:
            for index in range(len(self._board[faller.col()]) -1 , -1, -1):
                if self._board[faller.col()][index] == '   ':
                    self._board[faller.col()][index] == Jewel('freezing', faller.middle_color())
                    self._board[faller.col()][index - 1] == Jewel('freezing', faller.top_color())
                    faller._jewel_middle_row = index
                    faller._jewel_top_row = index - 1
        if faller.middle_row() != None and faller.top_row() == None:
            for index in range(len(self._board[faller.col()]) -1 , -1, -1):
                if self._board[faller.col()][index] == '   ':
                    self._board[faller.col()][index] = Jewel('freezing', faller.top_color())
                    faller._jewel_top_row = index
                    break
        

    def gravity(self):
        '''
        basic rule of the game
        if nothing under jewels, it will fall
        '''
        for col in self._board:
            for index in range(len(col) - 1):
                if col[len(col)- index - 2] != '   ' and col[len(col) - index - 1] == '   ':
                    col[len(col)- index - 2], col[len(col) - index - 1] = col[len(col) - index - 1], col[len(col)- index - 2]

        self._status = 'freezing'


    def gravity_again(self):
        '''
        gravity is performed until every jewels have things under them
        '''
        for col in self._board:
            for index in range(len(col) - 1):
                if col[len(col)- index - 2] != '   ' and col[len(col) - index - 1] == '   ':
                    self.gravity()

    def check(self, command: str) -> bool:
        '''
        check if the command can be executed
        return True or False
        '''
        faller = self._faller
        if faller == None:
            return False
        
        if command == 'descend':
            if self._board[faller.col()][faller.bottom_row() + 1] == '   ':
                return True
            
        if command == 'right':
            if faller.col() == self._col_number - 1:
                return False
            if self._board[faller.col() + 1][faller.bottom_row()] == '   ':
                if faller.middle_row() == None:
                    return True
                elif self._board[faller.col() + 1][faller.middle_row()] == '   ':
                    if faller.top_row() == None:
                        return True
                    elif self._board[faller.col() + 1][faller.top_row()] == '   ':
                        return True

        if command == 'left':
            if faller.col() == 0:
                return False
            if self._board[faller.col() - 1][faller.bottom_row()] == '   ':
                if faller.middle_row() == None:
                    return True
                elif self._board[faller.col() - 1][faller.middle_row()] == '   ':
                    if faller.top_row() == None:
                        return True
                    elif self._board[faller.col() - 1][faller.top_row()] == '   ':
                        return True

        if command == 'landing':
            if faller.bottom_row() == self.row() - 1:
                return True
            if self._board[faller.col()][faller.bottom_row() + 1] != '   ':
                return True
            
    def eliminate_and_find_match(self):
        '''
        eliminate jewels in match status
        find three or more jewels of the same color
        '''
        self.eliminate() 
        self.gravity()
        self.gravity_again()
        self.find_match()

    def descend_and_landing(self):
        '''
        descend the faller
        find out whether it is in landing status
        '''
        self.descend()
        if self.check('landing'):
            self.landing()

    def right_and_landing(self):
        '''
        move the faller to right
        find out whether it is in landing status
        '''
        self.right()
        if self.check('landing'):
            self.landing()

    def left_and_landing(self):
        '''
        move the faller to left
        find out whether it is in landing status
        '''
        self.left()
        if self.check('landing'):
            self.landing()

    def after_landing(self) -> bool:
        '''
        when status is in landing status
        change status -> freezing
        find three or more jewels of the same color
        find out whether game over
        '''
        self.freezing()
        self.eliminate_and_find_match()
        if self.game_status() == 'match':
            return False
        elif self.game_over():
            return True
        return False
        

    def print_board(self):
        '''
        print the board in special format
        '''
        for index in range(self.row()):
            print('|', end = '')
            for col in self._board:
                print(col[index], end = '')
            print('|')
        print(' ', end = '')
        for number in range(self.col() * 3):
            print('-', end = '')
        print(' ')

    def end_game(self):
        exit(0)

    def game_over(self) -> bool:
        '''
        judge whether game over
        return True of False
        '''
        faller = self._faller
        if self._board[faller.col()][faller.bottom_row()].status() == 'freezing':
            if faller.middle_row() == None:
                return True
            elif faller.top_row() == None:
                return True
        return False

