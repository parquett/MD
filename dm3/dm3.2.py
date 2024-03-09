def findCheapestPrice(n, flights, start, destination, k):
    # Create a dictionary to store the graph as an adjacency list
    graph = {}
    for f in flights:
        if f[0] not in graph:
            graph[f[0]] = []
        graph[f[0]].append((f[1], f[2]))

    # Initialize a queue for the breadth-first search
    queue = [(start, 0, 0)]  # (city, cost, stops)

    # Perform breadth-first search
    while queue:
        city, cost, stops = queue.pop(0)
        if city == destination:
            return cost  # Return the cost of the shortest path
        if stops <= k:  # Only consider paths with at most k stops
            for nei, price in graph.get(city, []):
                queue.append((nei, cost + price, stops + 1))

    return "no route"  # Return "no route" if no path was found

# Test the function
n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
start = 0
destination = 2
k = 1
print(findCheapestPrice(n, flights, start, destination, k))  # Output: 200
