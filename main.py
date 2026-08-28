#Import required libraries
import math
import heapq
import matplotlib.pyplot as pyplot

#Maze 2D Grid : "S" = Start, "G" = Goal, "." = Walkable cell, "#" = Wall
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'G']
]

#Coordinates of the start & goal cells
start = (0,0)
goal = (4,6)

#Print the maze row by row
for row in maze:
    print(' '.join(row))

#Print the start & goal coordinates
print("Start: ",start)  
print("Goal: ",goal)  

#A Function to find neighbour nodes
def find_neighbour(maze, position):
    row, column = position #Get the row & column of the current position

    #A node can be connected to its up, down, right or left neighbours
    directions = [
        (-1,0), #Up
        (1,0),  #Down
        (0,-1), #Left
        (0,1)   #Right
    ]
    neighbours = [] #Store the valid neighbouring positions

    #Check each possible direction
    for row_change, column_change in directions:
        new_row = row + row_change
        new_column = column + column_change

        #Ensure that the new position is inside the maze
        if 0 <= new_row < len(maze) and 0 <= new_column < len(maze[0]):
            #Add the position if it's not a wall
            if maze[new_row][new_column] != '#':
                neighbours.append((new_row, new_column))
    
    #Return all valid neighbouring positions
    return neighbours           


#Euclidean Heuristic 
#f(n) = g(n) + h(n) where: 
   #f(n) --> total estimated cost
   #g(n) --> actual cost from the start node to the current node
   #h(n) --> estimated cost from the current node to tha goal node "Euclidean distance"

#A function to calculate the Euclidean distance between a specific position and the goal
def heuristic(position, goal):
    row, column = position  #Get the row & column of the current position
    goal_row, goal_column = goal #Get the row & column of the goal
    
    #Euclidean distance formula
    return math.sqrt((row - goal_row)**2 + (column - goal_column) **2)


#A* Implementation
#A function to reconstruct the path from the goal
def reconstruct_path(prev_node, current):
    path = [current]  #
    
    #Follow the previous nodes till reaching the start
    while current in prev_node:
        current = prev_node[current]
        path.append(current)
    path.reverse() #Reverse the path to begin from the start node
    return path

#A function to find the shortest path from the start node to the goal, avoiding the walls 
def a_star(maze, start, goal):
    #If start & goal are the same, return the start immediately
    if start == goal:
        return [start]
    open_set = []  #Priority queue storing nodes that need to be explored
    heapq.heappush(open_set, (0, start))  #Add the start node with priority 0
    c_score = {start: 0}  #Store the actual cost from the start to each node
    prev_node = {}  #Store the previous node for each position
    
    while open_set:
        current_f, current = heapq.heappop(open_set) #Get the node with the lowest f-score
        
        #Stop searching if the goal is reached
        if current == goal:
            return reconstruct_path(prev_node, current)  #Reconstruct the shortest path
            
        #Find all valid neighbouring nodes
        neighbours = find_neighbour(maze, current)

        for neighbour in neighbours:
            g_score = c_score[current] + 1 #Cost of reaching the neighbour
            h_score = heuristic(neighbour,goal) #Euclidean heuristic
            f_score = g_score + h_score #Total f-score

            #Check for a better route to the neighbour
            if neighbour not in c_score or g_score < c_score[neighbour]:
                c_score[neighbour] = g_score  #Store the new cost
                prev_node[neighbour] = current  #Store the position from which the neighbour came from
                heapq.heappush(open_set, (f_score, neighbour))  #Add the neighbour to the priority queue
    return None  #If the goal can't be reached, return none


#A function to display the maze with the shortest path
def display_path(maze, path):
    display = [row[:] for row in maze]  #Copy of the maze, so the original remains unmodified

    #Mark each path position with a "*"
    for row, column in path:
        if display[row][column] not in ['S','G']:
            display[row][column] = '*'
    
    #Print the updated maze
    for row in display:
        print(' '.join(row)) 

    print("Path length: ", len(path) -1)

    #Legend           
    print("Legend:")
    print("S = Start")
    print("G = Goal")  
    print("# = Wall") 
    print("* = Shortest path")
    print(". = Walkable cell") 

                
#Graphical Visualization using Matplotlib
#A function to graphically visualize the maze & the shortest path
def visualize_maze(maze, path):
    #Get the number of rows & columns
    rows = len(maze)
    columns = lens(maze[0])

    #Create a figure
    fig, ax = plt.subplots(figsize=(8,6))

    #Draw the grid
    ax.set_xlim(0,columns)
    ax.set_ylim(0, rows)
    ax.set_xticks(range(columns + 1))
    ax.set_yticks(range(rows + 1))
    ax.grid(True)

    #Draw each cell
    for row in range(rows):
        for column in range(columns):
            #Set the cell color based on its type
            if maze[row][column] == '#':
                cell_color = 'black'
            elif (row, column) in path:
                cell_color = 'red'
            else:
                cell_color = 'white'    

            #Draw the cell
            ax.add_patch(
                plt.Rectangle(
                    (column,rows - row - 1),
                    1,
                    1,
                    facecolor=cell_color,
                    edgecolor='black'
                )
            )

#Mark the start and goal
start_row, start_column = start
goal_row, goal_column = goal

ax.text
(
    start_column + 0.5,
    rows - start_row - 0.5,
    'S',
    ha='center',
    va='center',
    fontsize=16
)

ax.text
(
    goal_column + 0.5,
    rows - goal_row - 0.5,
    'G',
    ha='center',
    va='center',
    fontsize=16
)

#Title
ax.set_title("Project 1 : A* Maze Solver")

#Remove axis labels
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()


#Test
path=a_star(maze,start,goal)
if path:
    print("Shortest path is: ", path)
    print("Maze with shortest path: ")
    display_path(maze,path)

    visualize_maze(maze, path)
else: 
    print("No path exists between start and goal")