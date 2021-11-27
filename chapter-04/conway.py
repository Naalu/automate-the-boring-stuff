# Conways Game of Life
import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# Create list of lists for the cells
nextCells = []
for x in range(WIDTH):
    column = []  # Create new column
    for y in range(HEIGHT):
        if random.randint(0, 3) == 0:
            column.append("#")  # Add living cell
        else:
            column.append(" ")  # Add dead cell
    nextCells.append(column)  # nextCells is a list of 'column' lists.

# Main program loop
while True:
    print("\n" * 5)  # Seperate steps w/ newlines
    currentCells = copy.deepcopy(nextCells)

    # Display cuurent cells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")  # Print the # or space
        print()  # newline added at end of row

    # Calculate next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates
            # `% WIDTH` ensures leftCoord is always between 0 and (WIDTH -1)
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top-left neighbor is alive
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1  # Top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top-right neighbor is alive
            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1  # Left neighbor is alive
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1  # Right neighbor is alive
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-left neighbor is alive
            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1  # Bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-right neighbor is alive

            # Set cell based on Conway's Game of Life Rules
            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                # Dead cells with 3 neighbors come to life
                nextCells[x][y] = "#"
            else:
                # Everything else dies or stays dead
                nextCells[x][y] = " "
    time.sleep(0.8)  # Add a pause to reduce flickering
