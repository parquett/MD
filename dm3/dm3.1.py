from collections import defaultdict

def canFinish(total_courses, prerequisites):
    # Create a graph in the form of an adjacency list
    graph = defaultdict(list)
    # Keep track of the indegree of each node (course)
    indegree = [0] * total_courses

    # Add edges to the graph and increase the indegree of the destination node
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1

    # Add all nodes with indegree 0 to the queue
    queue = []
    for i in range(total_courses):
        if indegree[i] == 0:
            queue.append(i)

    # Initialize the count of visited nodes
    count = 0

    # Perform a BFS
    while queue:
        # Pop a node from the queue and add it to the visited list
        node = queue.pop(0)
        count += 1
        # Decrease the indegree of each neighbor by 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            # If the indegree of a neighbor becomes 0, add it to the queue
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Return true if all nodes were visited, false otherwise
    return count == total_courses

total_courses = 4
prerequisites = [[0,1], [1,2], [2,3]]
print(canFinish(total_courses, prerequisites))
