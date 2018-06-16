from tkinter import *

GRID = []   # 2-D list to store the state of each co-ordinate on the board
SIZE = 10   # each cell will be dispayed graphically with a square SIZE x SIZE pixels


def main():
    global GRID
    getIn()
    buildGraph()


# read the input file to get the board and the number of generations to sim
def getIn():

    global M            # number of rows
    global N            # number of columns
    global GRID         # the grid for the game stored as 2-D list

    # read input board into 2-D global list 'GRID'
    with open('inLife.txt', 'r') as file:
        for line in file:
            if line not in ['\n','\r\n', '']:
                row = line.rstrip('\n\r')
                GRID.append(list(row))
        file.close()

    # set the globals for width and height of game board
    M = len(GRID)       # number of rows
    N = len(GRID[0])    # number of columns


# update the board to the next generation using the rules of the game
def nextGen():
    global GRID
    newGrid = [x[:] for x in GRID]      # make a copy of the grid
    for i in range(M):
        for j in range(N):
            numNeighs = getNeighbours(i,j)
            if GRID[i][j] == '1' and numNeighs <= 1:
                newGrid[i][j] = '0'     # dies of lonliness
            elif GRID[i][j] == '1' and numNeighs >= 4:
                newGrid[i][j] = '0'     # dies of overcrowding
            elif GRID[i][j] == '0' and numNeighs == 3:
                newGrid[i][j] = '1'     # new cell is born
    GRID = newGrid


# returns the number of neigbours of a co-ordinate that are alive
def getNeighbours(x,y):
    numNeighs = 0
    if y > 0 and GRID[x][y-1] == '1':
        numNeighs += 1
    if y < (N-1) and GRID[x][y+1] == '1':
        numNeighs += 1
    if x > 0 and GRID[x-1][y] == '1':
        numNeighs += 1
    if x < (M-1) and GRID[x+1][y] == '1':
        numNeighs += 1
    if x > 0 and y > 0 and GRID[x-1][y-1] == '1':
        numNeighs += 1
    if x < (M-1) and y > 0 and GRID[x+1][y-1] == '1':
        numNeighs += 1
    if x > 0 and y < (N-1) and GRID[x-1][y+1] == '1':
        numNeighs += 1
    if x < (M-1) and y < (N-1) and GRID[x+1][y+1] == '1':
        numNeighs += 1
    return numNeighs


# construct the graphic to be displayed
def buildGraph():
    global GRAPH
    width = SIZE*N
    height = SIZE*M
    root = Tk()
    root.overrideredirect(True)
    root.geometry('%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2))
    root.bind_all('<Escape>', lambda event: event.widget.quit())
    GRAPH = Canvas(root, width=width, height=height, background='white')
    GRAPH.after(40, update)
    GRAPH.pack()


# update the graphic with each new generation
def update():
    draw()
    GRAPH.after(500,update)
    nextGen()


# draw the board creating a square for each cell
# colour in the square with corresponding colour for alive or dead
# overwrites the previous graphic
def draw():
    GRAPH.delete(ALL)
    row = 0
    while row < len(GRID):
        col = 0
        while col < len(GRID[0]) and row < len(GRID):
            cell = GRID[row][col]
            startX = SIZE*col
            endX = startX+SIZE
            startY = SIZE*row
            endY = startY+SIZE
            # colour alive cells as steel blue 
            if cell == '1':     
                GRAPH.create_rectangle(startX,startY,endX,endY,fill="steelblue")
            # colour dead cells as aquamarine
            else:               
                GRAPH.create_rectangle(startX,startY,endX,endY,fill="aquamarine")
            col = col+1
        row = row+1
    GRAPH.update()


main()
