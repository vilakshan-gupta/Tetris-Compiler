import sys
sys.path.append('../')
from game_engine.engine import *

#PRIMITIVE:
Somename = 0
Someothername = 1
difficulty = 2
fg_color = 5
bg_color = 3
update_duration = 100
speed_increase_factor = 1
speed_decrease_factor = 1
direction = 1
shadow = 0
next = 0

#FUNCTIONS:
def Func2():
    Someothername = Someothername + Somename

def run():
    Somename = tetris_engine.move_piece(direction = 1)

def Func3():
    while 3 + 5 :
        while 3 + 5 :
            Someothername = 5


#ENGINE:
if __name__ == '__main__':
	tetris_engine = TetrisEngine(height = 20, width = 20, fg_color = fg_color, bg_color = bg_color, difficulty = difficulty, rotation_limit = 3, update_duration = update_duration)


