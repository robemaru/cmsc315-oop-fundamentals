# CMSC 315 - Unit 8 Discussion: Breadth-First Search (BFS)

## Overview
This assignment demonstrates graph traversal using Breadth-First Search (BFS) in Python. The graph is represented with an adjacency list, and BFS uses a queue to visit connected nodes level by level.

## Learning Objectives
* Represent graphs using adjacency lists.
* Implement Breadth-First Search.
* Use queues in graph traversal.
* Track visited nodes.
* Analyze BFS traversal behavior.
* Demonstrate edge cases.
* Apply graph traversal to a real-world example.

## Requirements Completed
* Created a graph using an adjacency list.
* Included more than 6 nodes.
* Included multiple connections between nodes.
* Displayed the graph structure.
* Implemented BFS with `collections.deque`.
* Used a starting node and displayed the traversal order.
* Added an additional connection and demonstrated the updated traversal.
* Demonstrated multiple edge cases:
  * Missing starting node
  * Empty graph
  * Disconnected/single-node situations
* Added comments explaining the queue, visited set, nodes, and edges.
* Included a real-world graph example.

## Graph Representation
The program models rooms in a small office building. Nodes represent rooms, and edges represent connections between rooms. The adjacency list stores each room and the rooms directly connected to it.

### Office Building Layout Matrix:
* **Lobby** ➡️ Office, Conference
* **Office** ➡️ Lobby, Kitchen, Hallway
* **Conference** ➡️ Lobby, Hallway
* **Kitchen** ➡️ Office, Hallway
* **Hallway** ➡️ Office, Conference, Kitchen, Exit
* **Exit** ➡️ Hallway
* **Storage** ➡️ No connections initially

*Note: The program later adds a connection between Storage and Kitchen to demonstrate how the graph and BFS traversal can change.*

## How BFS Works
BFS starts with a selected node and places it in a queue. It removes the first node from the queue, visits it, and adds its unvisited neighbors to the back of the queue. This process continues until the queue is empty.

The program uses:
* `deque` as the operational queue.
* A `visited` set to prevent duplicate loops or visits.
* A list named `order` to save the final traversal sequence.

Because BFS explores one level at a time, it is useful for finding the shortest number of edges between nodes in an unweighted graph structure.

## BFS vs. DFS
* **BFS (Breadth-First Search)** explores a graph level by level. It is a good choice when the goal is to find the shortest path in an unweighted graph or to find the closest matching nodes.
* **DFS (Depth-First Search)** explores as far as possible along one path before backtracking. DFS is useful for problems such as maze exploration, dependency analysis, and exploring hierarchical structures.

Neither algorithm is always better. The best choice depends entirely on the problem. BFS is especially useful when distance measured in the number of connections matters.

## Edge Cases
The program safely handles several distinct edge cases:
* **Missing Starting Node:** If the requested start node is not in the graph, the BFS function returns an empty list instead of causing an error.
* **Empty Graph:** If the graph has no active nodes, BFS returns an empty list.
* **Disconnected Nodes:** A BFS traversal only visits nodes reachable from its starting node. A disconnected part of a graph will not appear unless there is a connection to it.
* **Single-Node Graph:** A graph containing one node with no edges returns that single node when BFS starts there.

## Real-World Example
The office-room graph is a simple real-world example. A building can be represented as a graph where rooms are nodes and doorways or hallways are edges. BFS could be used to explore the building level by level or determine the fewest room-to-room connections needed to reach an exit.

Other real-world uses include:
* Social-network connections
* Computer-network routing
* Web-page crawling
* Finding nearby geographic locations
* Puzzle and game-state exploration

## Discussion Board Reflection
While completing this assignment, I learned how graphs can represent relationships and how adjacency lists store those relationships efficiently. I also learned how a queue controls the order of a BFS traversal and why a visited set is important for avoiding repeated visits and infinite loops in graphs with cycles. One challenge was making sure nodes were marked as visited at the correct time. I solved this by marking a node when it is added to the queue rather than waiting until it is removed. This prevents the same node from being added multiple times.

BFS and DFS both traverse graphs, but they behave differently. BFS explores nodes level by level, while DFS follows one path as deeply as possible before backtracking. BFS is useful for finding the shortest path in an unweighted graph, such as finding the fewest connections between people in a social network. DFS can be useful for maze exploration, dependency analysis, and exploring hierarchical structures. Overall, this assignment helped me understand how the choice of traversal algorithm depends on the problem being solved.

## How to Run
Run the Python file from your project directory:
```bash
python unit8_discussion.py
```

The program prints:
1. The original graph structure.
2. The first BFS traversal sequence.
3. The updated graph after adding a connection.
4. The updated BFS traversal output.
5. Results for the simulated edge cases.
6. A real-world graph explanation.

## GitHub Submission

https://github.com/robemaru/cmsc315-oop-fundamentals/tree/main/Unit8
