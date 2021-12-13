#Yifeng Xiong
#14648645
#class Jewel
#This is the most basic class. It defines the attributes of jewels in the game.
#Jewels have color and their own status: falling/ landing/ match/ freezing
#Each status has its own appearance.
#Jewel's color and status can be changed.

class Jewel:

    def __init__(self, status: str, color: str):
        self._status = status
        self._color = color

    def __str__(self):
        if self._status == 'falling':
            return '['+ self._color + ']'
        if self._status == 'landing':
            return '|'+ self._color + '|'
        if self._status == 'match':
            return '*'+ self._color + '*'
        if self._status == 'freezing':
            return ' '+ self._color + ' '

    def status(self) -> str:
        return self._status

    def color(self) -> str:
        return self._color

    def change_status(self, new_status: str):
        self._status = new_status

    def change_color(self, new_color: str):
        self._color = new_color
