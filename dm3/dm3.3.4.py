def dijkstra(graph, start):
    distances = [float("inf") for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]
    distances[start] = 0
    while True:
        shortest_distance = float("inf")
        shortest_index = -1
        for i in range(len(graph)):
            if distances[i] < shortest_distance and not visited[i]:
                shortest_distance = distances[i]
                shortest_index = i
        if shortest_index == -1:
            return distances
        for i in range(len(graph[shortest_index])):
            if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:
                distances[i] = distances[shortest_index] + graph[shortest_index][i]
        visited[shortest_index] = True



with open('matrix.txt', 'r') as f:
    data = f.read().splitlines()

people_list = data[0].split(" | ")
people_list[0] = people_list[0][5:]
nr_ppl = 20
people = {}
adj_matrix = []
array = []
for i in range(1, nr_ppl + 1):
    line, temp = data[i], []
    for j in line:
        if j.isdigit(): temp.append(int(j))
    adj_matrix.append(temp)
for i in range(20): array.append(dijkstra(adj_matrix, i))
for j in range(len(array)): people[people_list[j]] = float(sum(array[j]))

with open('influence.txt', 'r') as p:
    d = p.read().splitlines()
posts, res = {}, {}
for i in range(nr_ppl):
    line, temp = d[i], []
    temp = d[i].split(' : ')
    posts[temp[0]] = float(temp[1])
for n in range(20):
    res[people_list[n]] = list(people.items())[n][1] * (list(posts.items())[n][1] * 0.5)
result = sorted(res, key=res.get, reverse=True)
for t in result:
    print(t, int(res[t]))