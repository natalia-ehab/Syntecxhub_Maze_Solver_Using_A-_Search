# A* Maze Solver
A Python implementation of the A* search algorithm for finding the shortest path through a grid-based maze. The project represents the maze as nodes and uses the Euclidean distance as the heuristic function to efficiently guide the search from the start position to the goal while avoiding walls.

## Features
- Grid-based maze representation
- Start and goal positions
- Wall and walkable cells
- A* pathfinding algorithm
- Euclidean distance heuristic
- Shortest path reconstruction
- Handles unreachable goals
- Console-based path visualization
- Graphical maze visualization using Matplotlib

## Algorithm
A* evaluates each node using: f(n) = g(n) + h(n)
Where:
- "g(n)" is the actual cost from the start node.
- "h(n)" is the Euclidean distance from the current node to the goal.
- "f(n)" is the estimated total cost.

The Euclidean heuristic is calculated using: h(n) = √((x₁ - x₂)² + (y₁ - y₂)²)

## Requirements
- Python 3.x
- Matplotlib

Install matplotlib using: pip install -r requirements.txt

## How to Run
Run the following command from the project folder: python main.py

The program will find the shortest path and display the result in the console and graphically.

## Maze Symbols
# Symbol        Meaning
  S             Start
  G             Goal
  #             Wall
  .             Walkable cell
  *             Shortest path

## Project Structure
astar-maze-solver/
   main.py
   README.md
   requirements.txt
   .gitignore/

## Technologies
Python 
A* Search Algorithm
Euclidean Distance
Matplotlib