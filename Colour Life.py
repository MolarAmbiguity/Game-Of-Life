'''
Program By MolarAmbiguity, created at the 2014 South Coast Hackathon (29th and 30th Nov)
'''

from tkinter import *
import random

root = Tk()

CellList = []

def roll_cells():
    #print('called roll_cells')
    for i in range(2500):
        CellList.append(random.choice([0,(random.randint(500,1000))]))   
        NextGeneration = CellList

roll_cells()
NextGeneration = CellList

CellDraw =Canvas(root,bg='white',width=501,height=501)
root.wm_title('Life of Python)')
CellDraw.pack()

def dead_or_alive(CellToCheck):
    if CellList[CellToCheck] > 0:
        return 1
    else:
        return 0
    
def check_cell(Cell):
    #print('called check_cell')
    AliveCells = 0
    if Cell == 0:
        AliveCells = dead_or_alive(2499) + dead_or_alive(49) + dead_or_alive(99) + dead_or_alive(50) + dead_or_alive(51) + dead_or_alive(1) + dead_or_alive(2451) + dead_or_alive(2450)
    elif Cell == 49:
        AliveCells = dead_or_alive(2498) + dead_or_alive(48) + dead_or_alive(98) + dead_or_alive(99) + dead_or_alive(50) + dead_or_alive(0) + dead_or_alive(2450) + dead_or_alive(2499)
    elif Cell == 2450:
        AliveCells = dead_or_alive(2449) + dead_or_alive(2499) + dead_or_alive(49) + dead_or_alive(0) + dead_or_alive(1) + dead_or_alive(2451) + dead_or_alive(2401) + dead_or_alive(2400)
    elif Cell == 2499:
        AliveCells = dead_or_alive(2448) + dead_or_alive(2498) + dead_or_alive(48) + dead_or_alive(49) + dead_or_alive(0) + dead_or_alive(2450) + dead_or_alive(2400) + dead_or_alive(2449)
    elif Cell <49:
        AliveCells = dead_or_alive(Cell+2449) + dead_or_alive(Cell-1) + dead_or_alive(Cell+49) + dead_or_alive(Cell+50) + dead_or_alive(Cell+51) + dead_or_alive(Cell+1) + dead_or_alive(Cell+2451) + dead_or_alive(Cell+2450)
    elif Cell %50 == 0:
        AliveCells = dead_or_alive(Cell-1) + dead_or_alive(Cell+49) + dead_or_alive(Cell+99) + dead_or_alive(Cell+50) + dead_or_alive(Cell+51) + dead_or_alive(Cell+1) + dead_or_alive(Cell-49) + dead_or_alive(Cell-50)
    elif Cell >2450:
        AliveCells = dead_or_alive(Cell-51) + dead_or_alive(Cell-1) + dead_or_alive(Cell-2451) + dead_or_alive(Cell-2450) +dead_or_alive(Cell-2449) + dead_or_alive(Cell+1) + dead_or_alive(Cell-50) + dead_or_alive(Cell-51)
    elif Cell %50 == 49:
        AliveCells = dead_or_alive(Cell-51) + dead_or_alive(Cell-1) + dead_or_alive(Cell+49) + dead_or_alive(Cell+50) + dead_or_alive(Cell+1) + dead_or_alive(Cell-49) + dead_or_alive(Cell-99) + dead_or_alive(Cell-50)
    else:
       AliveCells = dead_or_alive(Cell-51) + dead_or_alive(Cell-50) + dead_or_alive(Cell-49) + dead_or_alive(Cell-1) + dead_or_alive(Cell+1) + dead_or_alive(Cell+49) + dead_or_alive(Cell+50) + dead_or_alive(Cell+51)
    return AliveCells

def next_board():
    #print('called next_board')
    for i in range(2500):
        if dead_or_alive(i) == 0 and check_cell(i) == 3:
            NextGeneration[i] = 1000
        elif dead_or_alive(i) == 1 and check_cell(i) < 2:
            NextGeneration[i] = 0
        elif dead_or_alive(i) == 1 and check_cell(i) > 3:
            NextGeneration[i]-=50
        else:
            NextGeneration[i] = CellList[i]


def update_cell(x,y,colour):
    #print('called update_cell')
    CellDraw.create_rectangle(x,y,x+10,y+10,fill=colour)
    CellDraw.pack()
    
def reset_board():
    x=y=2
    #print('called reset_board')
    for i in range(2500):
        update_cell(x,y,'white')
        if (i+1)%50==0:
            x+=10
            y-=490
        else:
            y+=10       


def populate_board():
    x=y=2
    #print('called populate_board')
    for i in range(2500):
        if NextGeneration[i] > 0:
            colour =hex(NextGeneration[i]*10)
            realcol = '#' + colour[2:]
            while len(realcol) < 7:
                realcol = realcol + '0'
            update_cell(x,y,realcol)
        else:
            update_cell(x,y,'black')
        if (i+1)%50==0:
            x+=10
            y-=490
        else:
            y+=10
       
reset_board()
populate_board()

def board():
    #print('called board')
    next_board()
    populate_board()
    root.after(1000,board)

root.after(1000,board)
root.mainloop()
