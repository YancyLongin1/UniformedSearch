"""
Created on Tue Dec  5 20:16:16 2024

@author: yancylongin

This project implements uninformed search algorithms to solve a sliding puzzle. The program integrates a sliding puzzle class, 
which simulates the puzzle's state, movement, and legality of actions, with search algorithms that find solutions to the puzzle.

### Features and Implementation
1. **Sliding Puzzle Representation**: 
   The puzzle is represented as a grid, initialized to a specific state, and scrambled by a given number of moves. The program tracks the current state, legal moves, and blank tile position.

2. **Search Algorithms**:
   - **Breadth-First Search (BFS)**: Ensures finding the shortest path but may use significant memory.
   - **Depth-First Search (DFS)**: Explores the deepest nodes first, but risks inefficiency or infinite loops.
   - **Depth-Limited Search (DLS)**: DFS with a depth limit to prevent infinite loops.
   - **Iterative Deepening Search (IDS)**: Combines the benefits of BFS and DFS, progressively deepening the search limit.

3. **Metrics and Results**:
   Each algorithm calculates:
   - **Time Taken**: How long it took to find a solution.
   - **Nodes Expanded**: Total states explored.
   - **Memory Usage**: Maximum nodes held in memory during execution.
   - **Action Sequence**: The series of moves to solve the puzzle.

This project is designed to study and compare the efficiency of various uninformed search techniques for solving combinatorial problems like sliding puzzles. The modular design allows easy integration of additional search algorithms or enhancements.
"""



from util.timeout import *
import util.search as search
import slidingpuzzle as sp
import argparse
import random


def dfs(p, initState):
    p.setState(initState)
    print(p, end="")
    startT = time.time()
    with timeout(15):
        path, cost, numExpanded = search.depthSearch(p)
    endT = time.time()
    atime = endT - startT
    return atime, path, cost, numExpanded

def dls(p, initState, limit):
    p.setState(initState)
    print(p, end="")
    startT = time.time()
    with timeout(15):
        path, cost, numExpanded = search.depthLimitedSearch(limit)
    endT = time.time()
    atime = endT - startT
    return atime, path, cost, numExpanded

def bfs(p, initState):
    p.setState(initState)
    print(p, end="")
    startT = time.time()
    with timeout(15):
        path, cost, numExpanded = search.breadthSearch(p)
    endT = time.time()
    atime = endT - startT
    return atime, path, cost, numExpanded

def iterative(p, initState, maxDepth):
    p.setState(initState)
    print(p, end="")
    startT = time.time()
    with timeout(15):
        path, cost, numExpanded = search.iterativeDeepening(p, maxDepth)
    endT = time.time()
    atime = endT - startT
    return atime, path, cost, numExpanded

def print_result(p, atime, path, cost, numExpanded):
    print("Time Taken:\t" + "{0:.5f}".format(atime))
    print("Nodes Expanded:\t" + str(numExpanded))
    print("Max Nodes in Memory:\t"+str(search.getMaxMemoryUse()))
    if path == [] and not p.isSolved():
        print("No solution found!")
    else:
        actionSeq = ""
        actions = {(0, 1): "E", (0, -1): "W", (1, 0): "S", (-1, 0): "N"}
        for a in path:
            actionSeq += actions[a] + " "
        print("Action sequence: " + actionSeq)

        print("Total cost: " + str(cost))
    print("-----------------------------")

def lab(args):
    depth = int(input("Enter the number of moves away from solved for the puzzle."))
    p = sp.SlidingPuzzle(args.rows, args.columns,0)
    startStates = p.getScrambledStates(depth, 1)
    initState = startStates[0]

    times = []
    expanded = []
    print("Performing breadth-first search:")
    try:
        atime, path, cost, numExpanded = bfs(p,initState)
        print_result(p, atime, path, cost, numExpanded)
    except:
        print("Search took too long")
        print("Tried expanding at least " + str(search.getTotalStates()) + " states.")
        print("Max memory usages at least "+ str(search.getMaxMemoryUse())+ " states.")
        print("-----------------------------")
    print("Performing depth-first search:")
    try:
        atime, path, cost, numExpanded = dfs(p,initState)
        print_result(p, atime, path, cost, numExpanded)
    except:
        print("Search took too long")
        print("Tried expanding at least " + str(search.getTotalStates()) + " states.")
        print("Max memory usages at least " + str(search.getMaxMemoryUse()) + " states.")
        print("-----------------------------")
    print("Performing depth-limited search:")
    try:
        atime, path, cost, numExpanded = dls(p,initState, depth + 3)
        print_result(p, atime, path, cost, numExpanded)
    except:
        print("Search took too long")
        print("Tried expanding at least " + str(search.getTotalStates()) + " states.")
        print("Max memory usages at least " + str(search.getMaxMemoryUse()) + " states.")
        print("-----------------------------")

    print("Performing iterative-deepening search:")
    try:
        atime, path, cost, numExpanded = iterative(p,initState, depth)
        print_result(p, atime, path, cost, numExpanded)
    except:
        print("Search took too long")
        print("Tried expanding at least " + str(search.getTotalStates()) + " states.")
        print("Max memory usages at least " + str(search.getMaxMemoryUse()) + " states.")
        print("-----------------------------")

def main():
    """Automatically solve randomly generated sliding puzzles."""
    parser = argparse.ArgumentParser(description='Solve sliding puzzles automatically or by hand.')
    parser.add_argument('-r', '--rows', type=int, default=3, help='the puzzle will have ROWS rows (default 3)')
    parser.add_argument('-c', '--columns', type=int, default=3, help='the puzzle will have COLUMNS columns (default 3)')
    args = parser.parse_args()
    lab(args)


if __name__ == "__main__":
    main()
