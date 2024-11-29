"""
Created on Tue Dec  5 20:16:16 2024

@author: yancylongin

### Project Description:
This module implements various uninformed search algorithms designed to solve state-space problems. These algorithms are particularly useful for navigating problem spaces, such as puzzles, mazes, and other combinatorial problems.

### Features:
1. **Search Algorithms**:
   - **Breadth-First Search (BFS)**: Explores all possible states at the current depth before proceeding to deeper states. Guarantees finding the shortest path in terms of steps but can consume significant memory.
   - **Depth-First Search (DFS)**: Explores as deep as possible along one branch before backtracking. Uses less memory than BFS but may not find the shortest path.
   - **Depth-Limited Search (DLS)**: A variant of DFS with a predefined depth limit to avoid infinite loops or excessive computation.
   - **Iterative Deepening Search (IDS)**: Combines the completeness of BFS with the memory efficiency of DFS by progressively deepening the search limit.
   - **A* Search**: Uses a heuristic to guide the search towards the goal, optimizing for both path cost and estimated cost to the goal.

2. **Performance Metrics**:
   - Tracks the number of nodes expanded during the search.
   - Monitors the maximum memory usage (number of nodes in the fringe) to evaluate algorithm efficiency.

3. **Priority Queue**:
   - Implements a heap-based priority queue for use in algorithms like A*, ensuring efficient retrieval of the next state to explore based on priority.

4. **Global Metrics**:
   - `getMaxMemoryUse()`: Returns the maximum number of nodes held in memory during a search.
   - `getTotalStates()`: Returns the total number of states expanded during the search.

### Implementation Details:
- **Problem State Representation**:
   The algorithms interact with a `problem` object that provides methods to retrieve the current state, generate successors, and check if a goal state has been reached.

- **Heuristics**:
   The A* search relies on an external heuristic function to estimate the cost to the goal. This heuristic is passed as a parameter to the `aStarSearch` function.

- **Scalability**:
   Each algorithm is implemented to handle large state spaces, with safeguards to manage memory and processing time. Depth-limited and iterative-deepening searches are particularly useful for addressing scalability.

### Use Cases:
This module is ideal for solving a wide range of problems, including:
   - Sliding puzzles.
   - Route planning in navigation systems.
   - Game AI for decision-making.
   - Any problem that can be represented as a state-space graph.

This file is part of a broader project aimed at studying search algorithms' behavior and efficiency in solving complex problems.
"""


import heapq

class PriorityQueue:
    '''A priority queue. Each item in the queue is associated with a priority. The queue gives efficient access to the minimum priority item.'''
    def __init__(self):
        self.__heap = []

    def push(self, item, priority):
        pair = (priority, item)
        heapq.heappush(self.__heap, pair)

    def pop(self):
        (priority, item) = heapq.heappop(self.__heap)
        return item, priority

    def isEmpty(self):
        return len(self.__heap) == 0

    def getSize(self):
        return len(self.__heap)

maxMemoryUse = 0
totalStates = 0
def aStarSearch(problem, heuristic):
    global maxMemoryUse
    global totalStates
    maxMemoryUse = 0
    totalStates = 0
    fringe = PriorityQueue()
    visited = {}
    inFringe = {}
    startState = problem.getState()
    fringe.push((startState, [], 0, problem.isSolved()), heuristic.eval(startState))
    inFringe[startState] = True
    numExpanded = 0
    while not fringe.isEmpty():
        s, score = fringe.pop()
        # note: s is (state, path, cost, solved or not)
        inFringe[s[0]] = False
        if s[3]:
            return s[1], s[2], numExpanded
        elif s[0] not in visited:
            numExpanded += 1
            visited[s[0]] = True
            successors = problem.getSuccessors(s[0])
            # note: Each successor is (state, action to get there, cost to get there, goal or not)
            for succ in successors:
                if succ[0] not in visited:# and succ[0] not in inFringe:
                    fringe.push((succ[0], s[1] + [succ[1]], s[2] + succ[2], succ[3]), s[2] + succ[2] + heuristic.eval(succ[0]))
                    inFringe[succ[0]] = True
            if fringe.getSize() > maxMemoryUse:
                maxMemoryUse = fringe.getSize()
            totalStates = numExpanded
    return [], float("inf"), numExpanded


def getMaxMemoryUse():
    return maxMemoryUse

def getTotalStates():
    return totalStates
def breadthSearch(problem):
    global maxMemoryUse
    global totalStates
    maxMemoryUse = 0
    totalStates = 0
    fringe = []
    visited = {}
    inFringe = {}
    startState = problem.getState()
    fringe.append((startState, [], 0, problem.isSolved()))
    inFringe[startState] = True
    numExpanded = 0
    while len(fringe) != 0:
        s = fringe.pop(0)
        #print("Examining: \n"+s[0] + ", "+str(s[1]) + ", "+str(s[2]) + ", "+str(s[3]))
        # note: s is (state, path, cost, solved or not)
        inFringe[s[0]] = False
        if s[3]:
            return s[1], s[2], numExpanded
        elif s[0] not in visited:
            numExpanded += 1
            totalStates = numExpanded
            visited[s[0]] = True
            successors = problem.getSuccessors(s[0])
            # note: Each successor is (state, action to get there, cost to get there, goal or not)
            for succ in successors:
                if succ[0] not in visited:# and succ[0] not in inFringe:
                    #print("Adding to queue: \n"+succ[0]+" with cost "+str(s[2] + succ[2]))
                    #  fringe.push((succ[0], s[1] + [succ[1]], s[2] + succ[2], succ[3]), s[2] + succ[2] + heuristic.eval(succ[0]))
                    fringe.append((succ[0], s[1] + [succ[1]], s[2] + succ[2], succ[3]))
                    if len(fringe) > maxMemoryUse:
                        maxMemoryUse = len(fringe)
                    inFringe[succ[0]] = True
    return [], float("inf"), numExpanded

def depthSearch(problem):
    global maxMemoryUse
    global totalStates
    maxMemoryUse = 0
    totalStates = 0
    fringe = []
    visited = {}
    inFringe = {}
    startState = problem.getState()
    fringe.append((startState, [], 0, problem.isSolved()))
    inFringe[startState] = True
    numExpanded = 0
    while len(fringe) != 0:
        s = fringe.pop()
        inFringe[s[0]] = False
        if s[3]:
            return s[1], s[2], numExpanded
        elif s[0] not in visited:
            numExpanded += 1
            totalStates = numExpanded
            visited[s[0]] = True
            successors = problem.getSuccessors(s[0])
            for succ in successors:
                if succ[0] not in visited:# and succ[0] not in inFringe:
                    fringe.append((succ[0], s[1] + [succ[1]], s[2] + succ[2], succ[3]))
                    inFringe[succ[0]] = True
                    if len(fringe) > maxMemoryUse:
                        maxMemoryUse = len(fringe)
    return [], float("inf"), numExpanded

def depthLimitedSearch(problem, maxDepth, reset = True):
    global maxMemoryUse
    global totalStates
    if reset:
        maxMemoryUse = 0
        totalStates = 0
    fringe = []
    visited = {}
    inFringe = {}
    startState = problem.getState()
    fringe.append((startState, [], 0, problem.isSolved(), 0))
    inFringe[startState] = True
    numExpanded = 0
    while len(fringe) != 0:
        s = fringe.pop()
        inFringe[s[0]] = False
        if s[3]:
            return s[1], s[2], numExpanded
        elif s[0] not in visited and s[4] < maxDepth:
            numExpanded += 1
            totalStates += 1
            visited[s[0]] = True
            successors = problem.getSuccessors(s[0])
            for succ in successors:
                if succ[0] not in visited:# and succ[0] not in inFringe:
                    fringe.append((succ[0], s[1] + [succ[1]], s[2] + succ[2], succ[3], s[4]+1))
                    inFringe[succ[0]] = True
                    if len(fringe) > maxMemoryUse:
                        maxMemoryUse = len(fringe)
    return [], float("inf"), numExpanded

def iterativeDeepening(problem, maxDepth):
    global maxMemoryUse
    global totalStates
    maxMemoryUse = 0
    totalStates = 0
    state = problem.getState()
    numExpanded = 0
    depth = 1
    while depth <= maxDepth:
        problem.setState(state)
        path, cost, expanded = depthLimitedSearch(problem, depth, False)
        numExpanded += expanded
        if len(path) > 0:
            return path, cost, numExpanded
        depth += 1
    return [], float("inf"), numExpanded