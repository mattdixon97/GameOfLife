# Conway’s Game of Life

## Overview

The Game of Life was invented in 1970 by James Conway, a British mathematician at the University of
Cambridge. The game is a zero-player game as the outcome is decided by the initial configuration of the
game board. The game board is an m x n grid consisting of cells that are either alive or dead. The game
progresses in generations as cells are born and die based on a set of rules.

## Rules

The rules determining whether a cell is born or dies are based on the current state of the cell and the
number of its neighbours that are alive. A cell is considered “a neighbour” if it is one of the 8 cells
directly adjacent to the cell.

State of Cell      | Number of Neighbours      | New State
----- | ----- | -----
1 (Alive) |     0 or 1 | 0, Dies of loneliness
1 (Alive) |      2 or 3 | 1, Lives
1 (Alive)  |      4, 5, 6, 7, or 8  | 0, Dies of overcrowding
0 (Dead) |     3 | 1, Is born
0 (Dead) |     0, 1, 2, 4, 5, 6, 7, 8    | 0, Remains dead


## Input

The program requires a single text file named ‘inLife.txt’ as input. In this file, the first line should be a
positive integer representing the number of generations to simulate. The rest of the file should consist
of an m x n grid of the initial state of the game board. A ‘0’ is used to represent a dead cell and a ‘1’ is
used to represent an alive cell. The input file is read by the program using the function getIn(). The dimensions of the board
are stored in the globals M and N. Finally, the board itself is stored in a global two dimensional list GRID
where GRID[0]0] represents the top-left most cell on the board.

## Generations

To generate the next generation, the program makes a call to the function ​ nextGen(). First, a copy of the
grid called newGrid. Next, it transverses each cell of newGrid and determines the number of neighbors
of the cell. It accomplishes this by making a call to the function getNeighbours(x,y). The function takes
two parameters representing the coordinate of the cell. It counts the number of alive neighbours in the
eight surrounding cells and returns the number. Using the rules of Game of Life as specified above, it
determines the new state of the cell.

## Output

The board is outputted graphically using tkinter. buildGraph() is initially called and constructs the graphic
to be displayed. Next, the update() function is called. While there are still generations to be simulated,
draw(), draws the board creating a square for each cell. It then colours in the square with the
corresponding colour for alive or dead depending on the state of the cell. After displaying the board for
a specified amount of time, it process the next generation and updates the board.
