<h1>Uniformed Search with Sliding Puzzle</h1>

<h2>Description</h2>
This project implements uninformed search algorithms on a classic sliding puzzle. The program explores **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, **Depth-Limited Search**, and **Iterative-Deepening Search (IDS)** to solve puzzles of varying complexities. It includes visualizations for human interaction and benchmarks the performance of these algorithms.

<h2>Features</h2>
The Uniformed Search Sliding Puzzle project includes:
- A customizable sliding puzzle representation.
- Four uninformed search algorithms: BFS, DFS, Depth-Limited Search, and IDS.
- Performance metrics: Time taken, nodes expanded, and memory usage.
- A visual sliding puzzle for human interaction using images.
- Automatic solving of puzzles with customizable depth and size.

<h2>Languages and Libraries Used</h2>
- <b>Python</b>
- <b>argparse</b> (for command-line arguments)
- <b>Custom Utilities</b> (`util.cImage`, `util.search`, `util.timeout`)

<h2>Environment Used</h2>
- <b>Spyder</b> (for development and testing)
- <b>Command Line</b> (for executing the program)

<h2>Program Walk-Through</h2>

<p align="center">
<h3>1. Puzzle Initialization</h3>
The puzzle starts with a customizable grid size and a scrambled state determined by the number of moves from the solved state. This ensures a reproducible complexity level for testing the search algorithms. Below is an example of a 3x3 puzzle of an octupus: <br/>
<img src="https://i.imgur.com/K51iH3W.png" height="80%" width="80%" alt="Puzzle Initialization"/>
<img src="https://i.imgur.com/0uIwK23.png" height="80%" width="80%" alt="Puzzle Initialization"/>
<br />
<br />

<h3>2. Breadth-First Search (BFS)</h3>
BFS explores the shallowest nodes first, ensuring it finds the shortest solution. However, it uses significant memory in larger puzzles. The following code and metrics are displayed:
<br/>
<img src="https://i.imgur.com/BAAVQai.png" height="80%" width="80%" alt="Breadth-First Search Output"/>
<img src="https://i.imgur.com/NI6nE9t.png" height="80%" width="80%" alt="Breadth-First Search Output"/>
<br />
<br />

<h3>3. Depth-First Search (DFS)</h3>
DFS explores as deeply as possible before backtracking. While it uses less memory, it risks getting stuck in infinite loops or taking too long for deep puzzles. Example output:
<br/>
<img src="https://i.imgur.com/PEmn3dg.png" height="80%" width="80%" alt="Depth-First Search Output"/>
<img src="https://i.imgur.com/7ds4Rmh.png" height="80%" width="80%" alt="Breadth-First Search Output"/>
<br />
<br />

<h3>4. Depth-Limited Search</h3>
Depth-Limited Search adds a depth constraint to DFS to prevent infinite loops. However, if the depth is insufficient, it may fail to find a solution. Example metrics:
<br/>
<img src="https://i.imgur.com/d8v0b4m.png" height="80%" width="80%" alt="Depth-Limited Search Output"/>
<img src="https://i.imgur.com/IkzdP8h.png" height="80%" width="80%" alt="Breadth-First Search Output"/>
<br />
<br />

<h3>5. Iterative-Deepening Search (IDS)</h3>
IDS combines the benefits of BFS and DFS by performing a series of depth-limited searches with increasing depth limits. It ensures completeness and optimality while managing memory efficiently. Example metrics:
<br/>
<img src="https://i.imgur.com/ttyMkwk.png" height="80%" width="80%" alt="Iterative-Deepening Search Output"/>
<img src="https://i.imgur.com/O5ME5DX.png" height="80%" width="80%" alt="Breadth-First Search Output"/>
<br />
</p>

