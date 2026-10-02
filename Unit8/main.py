from collections import deque

"""
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)

This program demonstrates:
- Graph representation with an adjacency list
- Breadth-First Search using a queue
- Visited-node tracking
- BFS traversal order
- Edge cases such as missing start nodes and empty graphs
- A real-world graph example
"""


def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS).

    The queue is used because BFS explores the graph level by level.
    A visited set prevents the same node from being processed repeatedly,
    which is especially important when the graph contains cycles.

    Returns:
        A list containing nodes in the order they were visited.
        Returns an empty list when the start node does not exist.
    """
    if not graph:
        return []

    if start not in graph:
        return []

    queue = deque([start])
    visited = {start}
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def display_graph(graph):
    """Display the adjacency-list representation of the graph."""
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors) if neighbors else 'No connections'}")


def main():
    print("==========================================")
    print("UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH")
    print("==========================================")

    # TODO (Student): CREATE A GRAPH
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.
    #
    # Completed: This graph represents rooms in a small office.
    # Each key is a room/node and each value is a list of connected rooms/edges.
    graph = {
        "Lobby": ["Office", "Conference"],
        "Office": ["Lobby", "Kitchen", "Hallway"],
        "Conference": ["Lobby", "Hallway"],
        "Kitchen": ["Office", "Hallway"],
        "Hallway": ["Office", "Conference", "Kitchen", "Exit"],
        "Exit": ["Hallway"],
        "Storage": []
    }

    print("\n=== GRAPH STRUCTURE ===")
    display_graph(graph)

    # TODO (Student): BFS TRAVERSAL
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge and demonstrate the updated traversal.
    #
    # Completed: Start at Lobby. BFS visits the closest rooms first.
    start_node = "Lobby"

    print("\n=== BFS TRAVERSAL ===")
    print(f"Starting node: {start_node}")

    traversal_order = bfs(graph, start_node)
    print("BFS traversal order:")
    print(" -> ".join(traversal_order))

    # Add an additional edge/node connection and demonstrate the change.
    graph["Storage"].append("Kitchen")
    graph["Kitchen"].append("Storage")

    print("\n=== UPDATED GRAPH ===")
    display_graph(graph)

    updated_order = bfs(graph, start_node)
    print("\nUpdated BFS traversal from Lobby:")
    print(" -> ".join(updated_order))

    # TODO (Student): EDGE CASES
    # Demonstrate at least two edge cases.
    #
    # Examples:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Completed: The program demonstrates a missing start node,
    # an empty graph, and a disconnected node.
    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: missing starting node
    missing_result = bfs(graph, "MissingRoom")
    print("Missing start node:", missing_result)

    # Edge case 2: empty graph
    empty_result = bfs({}, "Lobby")
    print("Empty graph:", empty_result)

    # Edge case 3: disconnected node
    disconnected_result = bfs(graph, "Storage")
    print("Disconnected node after adding Storage-Kitchen edge:", disconnected_result)

    # Edge case 4: graph with one node
    single_node_result = bfs({"OnlyRoom": []}, "OnlyRoom")
    print("Single-node graph:", single_node_result)

    print("\n=== REAL-WORLD GRAPH EXAMPLE ===")
    print("The graph above models rooms in an office building.")
    print("BFS can be used to explore connected rooms level by level,")
    print("such as finding the fewest room-to-room connections to an exit.")


if __name__ == "__main__":
    main()
