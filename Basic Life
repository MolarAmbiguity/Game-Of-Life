'''
Program By MolarAmbiguity, created at the 2014 Bega Hackathon (29th and 30th Nov)
'''

from tkinter import *
import random

root = Tk()

CellList = []
Running = 0

def roll_cells():
    #print('called roll_cells')
    for i in range(2500):
        CellList.append(random.choice([1,0,0,0,0,0,0,0,0,0,0]))   
        NextGeneration = CellList

roll_cells()
NextGeneration = CellList

CellDraw =Canvas(root,bg='white',width=501,height=501)
root.wm_title('Classic Life')
CellDraw.pack()

def check_cell(Cell):
    #print('called check_cell')
    AliveCells = 0
    if Cell == 0:
        AliveCells = CellList[2499] + CellList[49] + CellList[99] + CellList[50] + CellList[51] + CellList[1] + CellList[2451] + CellList[2450]
    elif Cell == 49:
        AliveCells = CellList[2498] + CellList[48] + CellList[98] + CellList[99] + CellList[50] + CellList[0] + CellList[2450] + CellList[2499]
    elif Cell == 2450:
        AliveCells = CellList[2449] + CellList[2499] + CellList[49] + CellList[0] + CellList[1] + CellList[2451] + CellList[2401] + CellList[2400]
    elif Cell == 2499:
        AliveCells = CellList[2448] + CellList[2498] + CellList[48] + CellList[49] + CellList[0] + CellList[2450] + CellList[2400] + CellList[2449]
    elif Cell <49:
        AliveCells = CellList[Cell+2449] + CellList[Cell-1] + CellList[Cell+49] + CellList[Cell+50] + CellList[Cell+51] + CellList[Cell+1] + CellList[Cell+2451] + CellList[Cell+2450]
    elif Cell %50 == 0:
        AliveCells = CellList[Cell-1] + CellList[Cell+49] + CellList[Cell+99] + CellList[Cell+50] + CellList[Cell+51] + CellList[Cell+1] + CellList[Cell-49] + CellList[-50]
    elif Cell >2450:
        AliveCells = CellList[Cell-51] + CellList[Cell-1] + CellList[Cell-2451] + CellList[Cell-2450] + CellList[Cell-2449] + CellList[Cell+1] + CellList[Cell-50] + CellList[Cell-51]
    elif Cell %50 == 49:
        AliveCells = CellList[Cell-51] + CellList[Cell-1] + CellList[Cell+49] + CellList[Cell+50] + CellList[Cell+1] + CellList[Cell-49] + CellList[Cell-99] + CellList[Cell-50]
    else:
       AliveCells = CellList[Cell-51] + CellList[Cell-50] + CellList[Cell-49] + CellList[Cell-1] + CellList[Cell+1] + CellList[Cell+49] + CellList[Cell+50] + CellList[Cell+51]
    return AliveCells

def next_board():
    #print('called next_board')
    for i in range(2500):
        if CellList[i] == 0 and check_cell(i) == 3:
            NextGeneration[i] = 1
        elif CellList[i] == 1 and check_cell(i) < 2:
            NextGeneration[i] = 0
        elif CellList[i] == 1 and check_cell(i) > 3:
            NextGeneration[i] = 0
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
        if NextGeneration[i] == 0:
            update_cell(x,y,'black')
        else:
            update_cell(x,y,'yellow')
        if (i+1)%50==0:
            x+=10
            y-=490
        else:
            y+=10
       
reset_board()
